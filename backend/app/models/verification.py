"""
Verification result model
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VerificationResult(BaseModel):
    post_id: str
    cleaned_claim: str
    verdict: str  # "TRUE", "FALSE", "MISLEADING", "OUTDATED", "INSUFFICIENT_EVIDENCE"
    truth_score: float  # 0-100
    confidence: float  # 0-100
    suspicious_claim: str
    actual_fact: str
    evidence_source: str
    source_date: Optional[str] = None
    explanation: str
    current_status: str
    historical_context: Optional[str] = None
    is_outdated: bool = False
    was_previously_true: bool = False

class VerifyPostRequest(BaseModel):
    post_id: str
    content: str
