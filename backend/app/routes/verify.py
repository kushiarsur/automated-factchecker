"""
Fact verification routes
"""
from fastapi import APIRouter
from typing import Dict

from ..models.verification import VerifyPostRequest, VerificationResult
from ..services.preprocess import clean_text, normalize_claim
from ..services.claim_detector import contains_claim
from ..services.claim_extractor import extract_main_claim
from ..services.retrieval import get_retriever
from ..services.verifier import get_verifier
from ..services.freshness_check import get_freshness_checker
from ..services.historical_context import get_historical_context_service

router = APIRouter(tags=["verify"])

@router.post("", response_model=VerificationResult)
async def verify_post(request: VerifyPostRequest):
    content = request.content
    cleaned_content = clean_text(content)
    has_claim, claim_confidence = contains_claim(cleaned_content)

    if not has_claim:
        if not retrieved_facts:
            return VerificationResult(
            post_id=request.post_id,
            cleaned_claim=main_claim,
            verdict="INSUFFICIENT_EVIDENCE",
            truth_score=50.0,
            confidence=35.0,
            suspicious_claim=main_claim,
            actual_fact="This claim is not in our verified facts database. It may be true but we cannot confirm it with our current data.",
            evidence_source="Fact Database",
            explanation="We detected a factual claim but it doesn't match any entry in our verified facts database. Try claims about well-known topics like space myths, health facts, or technology.",
            current_status="Claim detected but unverified — not in database",
            is_outdated=False,
            was_previously_true=False
        )
        

    main_claim = extract_main_claim(cleaned_content)
    normalized = normalize_claim(main_claim)

    retriever = get_retriever()
    retrieved_facts = retriever.retrieve(normalized, top_k=3)

    if not retrieved_facts:
        return VerificationResult(
            post_id=request.post_id, cleaned_claim=main_claim,
            verdict="INSUFFICIENT_EVIDENCE", truth_score=50.0, confidence=40.0,
            suspicious_claim=main_claim,
            actual_fact="No matching verified facts found in database.",
            evidence_source="Fact Database",
            explanation="This claim could not be verified against our database. It may require manual fact-checking.",
            current_status="Unverified - insufficient evidence",
            is_outdated=False, was_previously_true=False
        )

    best_fact, similarity_score = retrieved_facts[0]

    verifier = get_verifier()
    nli_verdict, nli_confidence = verifier.verify(normalized, best_fact['verified_fact'])

    freshness_checker = get_freshness_checker()
    is_fresh, staleness_reason = freshness_checker.check_freshness(best_fact, best_fact.get('category'))

    history_service = get_historical_context_service()

    verdict = _determine_verdict(best_fact['truth_value'], nli_verdict, is_fresh, best_fact.get('was_previously_true', False))
    truth_score = _calculate_truth_score(verdict, best_fact, nli_confidence)
    confidence = (similarity_score * 50) + (nli_confidence * 50)

    historical_context = None
    if verdict == "OUTDATED" or best_fact.get('was_previously_true'):
        historical_context = history_service.get_historical_context(main_claim, best_fact, verdict)

    explanation = _generate_explanation(verdict, best_fact, nli_verdict, is_fresh, staleness_reason)
    current_status = _get_current_status(verdict, best_fact)

    return VerificationResult(
        post_id=request.post_id, cleaned_claim=main_claim,
        verdict=verdict, truth_score=truth_score, confidence=confidence,
        suspicious_claim=main_claim, actual_fact=best_fact['verified_fact'],
        evidence_source=best_fact['source'], source_date=best_fact.get('source_date'),
        explanation=explanation, current_status=current_status,
        historical_context=historical_context,
        is_outdated=(verdict == "OUTDATED"),
        was_previously_true=best_fact.get('was_previously_true', False)
    )

def _determine_verdict(truth_value, nli_verdict, is_fresh, was_previously_true):
    if truth_value == "OUTDATED":
        return "OUTDATED"
    if not is_fresh and was_previously_true:
        return "OUTDATED"
    if nli_verdict == "REFUTES" and was_previously_true:
        return "OUTDATED"
    if truth_value == "TRUE":
        return "TRUE" if nli_verdict == "SUPPORTS" else "MISLEADING"
    elif truth_value == "FALSE":
        return "FALSE" if nli_verdict == "REFUTES" else "MISLEADING"
    elif truth_value == "MISLEADING":
        return "MISLEADING"
    return "INSUFFICIENT_EVIDENCE"

def _calculate_truth_score(verdict, fact, nli_confidence):
    base_scores = {"TRUE": 85.0, "FALSE": 15.0, "MISLEADING": 40.0, "OUTDATED": 45.0, "INSUFFICIENT_EVIDENCE": 50.0}
    base = base_scores.get(verdict, 50.0)
    adjustment = (fact.get('confidence', 0.8) * nli_confidence) * 10
    if verdict == "TRUE":
        return round(min(100, base + adjustment), 1)
    elif verdict == "FALSE":
        return round(max(0, base - adjustment), 1)
    return round(base, 1)

def _generate_explanation(verdict, fact, nli_verdict, is_fresh, staleness_reason):
    explanations = {
        "TRUE": "This claim is supported by verified evidence. The information matches credible sources.",
        "FALSE": "This claim contradicts verified facts. The statement is not supported by credible evidence.",
        "MISLEADING": "This claim is misleading. While it may contain some elements of truth, the overall statement misrepresents the facts.",
        "OUTDATED": "This claim may have been true in the past, but the information is now outdated. Circumstances have changed.",
        "INSUFFICIENT_EVIDENCE": "There is not enough verified evidence to confirm or deny this claim."
    }
    explanation = explanations.get(verdict, "Unable to verify this claim.")
    if not is_fresh and staleness_reason:
        explanation += f" {staleness_reason}"
    return explanation

def _get_current_status(verdict, fact):
    statuses = {
        "TRUE": "Verified as accurate",
        "FALSE": "Verified as false",
        "MISLEADING": "Partially true but misleading",
        "OUTDATED": "Information is outdated",
    }
    return statuses.get(verdict, "Unable to verify")
