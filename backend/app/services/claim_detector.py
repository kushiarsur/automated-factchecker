"""
Claim detection service
"""
import re
from typing import Tuple

FACTUAL_INDICATORS = [
    r'\bfact\b', r'\btrue\b', r'\bfalse\b', r'\bproven\b',
    r'\bstud(y|ies)\b', r'\bresearch\b', r'\bscientists?\b',
    r'\bexperts?\b', r'\breport(s|ed)?\b', r'\baccording to\b',
    r'\bis\b', r'\bare\b', r'\bwas\b', r'\bwere\b',
    r'\bshows?\b', r'\breveals?\b', r'\bconfirms?\b',
    r'\b\d+%\b', r'\b\d+ (people|percent|users)\b',
    r'\bhas\b', r'\bhave\b', r'\bhad\b', r'\bcan\b',
    r'\bcauses?\b', r'\bmakes?\b', r'\bcontains?\b',
    r'\blocated\b', r'\bfound\b', r'\bknown\b'
]

OPINION_INDICATORS = [
    r'\bi think\b', r'\bi believe\b', r'\bin my opinion\b',
    r'\bprobably\b', r'\bmaybe\b', r'\bmight\b',
    r'\bfeels? like\b', r'\bseems?\b', r'\bappears?\b',
    r'\bshould\b', r'\bamazing\b', r'\bawesome\b', r'\blove\b'
]

def contains_claim(text: str) -> Tuple[bool, float]:
    text_lower = text.lower()

    # Very short pure opinion/greeting — skip
    if len(text_lower.split()) <= 2:
        return False, 0.2

    factual_score = sum(1 for p in FACTUAL_INDICATORS if re.search(p, text_lower))
    opinion_score = sum(1 for p in OPINION_INDICATORS if re.search(p, text_lower))

    # Pattern: "X is/are/was Y" — basic factual statement
    basic_claim = bool(re.search(r'\b\w+\s+(is|are|was|were|has|have)\s+\w+', text_lower))

    # Pattern: adjective/noun describing something (sky is blue, water is wet)
    descriptive_claim = bool(re.search(r'\bthe\s+\w+\s+(is|are)\s+\w+', text_lower))

    # Has named entity (capitalized word) + verb
    named_entity_claim = bool(re.search(r'[A-Z][a-z]+.*\b(is|are|was|were|has|have)\b', text))

    # Numbers suggest factual content
    has_numbers = bool(re.search(r'\b\d+\b', text_lower))

    # Score calculation
    if descriptive_claim or named_entity_claim:
        return True, 0.75

    if basic_claim:
        return True, 0.70

    if factual_score >= 2 and factual_score > opinion_score:
        return True, min(0.9, 0.5 + factual_score * 0.1)

    if factual_score >= 1 and has_numbers:
        return True, 0.65

    if factual_score >= 1 and opinion_score == 0:
        return True, 0.60

    return False, 0.3

def is_newsworthy(text: str) -> bool:
    news_keywords = ['breaking', 'news', 'report', 'announced', 'today',
                     'yesterday', 'official', 'statement', 'declared']
    return any(kw in text.lower() for kw in news_keywords)