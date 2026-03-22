"""
Claim extraction service
"""
import re
from typing import List

def extract_main_claim(text: str) -> str:
    """Extract the main factual claim from text"""
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        return text

    scored = [(s, _score_claim_sentence(s)) for s in sentences]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0]

def _score_claim_sentence(sentence: str) -> float:
    score = 0.0
    sent_lower = sentence.lower()
    if re.search(r'\d+', sentence):
        score += 0.3
    factual_verbs = ['is', 'are', 'was', 'were', 'contains', 'shows', 'proves']
    if any(v in sent_lower.split() for v in factual_verbs):
        score += 0.4
    if re.search(r'\b[A-Z][a-z]+\b', sentence):
        score += 0.2
    if len(sentence.split()) >= 5:
        score += 0.1
    return min(score, 1.0)

def extract_entities(text: str) -> List[str]:
    entities = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', text)
    return list(set(entities))
