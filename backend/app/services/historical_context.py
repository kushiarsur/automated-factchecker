"""
Historical context service
"""
from typing import Optional, Dict
from dateutil import parser as date_parser

class HistoricalContextService:
    def get_historical_context(self, claim: str, fact: Dict, current_status: str) -> Optional[str]:
        was_previously_true = fact.get('was_previously_true', False)
        historical_context = fact.get('historical_context')
        if not was_previously_true:
            return None
        if historical_context:
            return historical_context
        source_date_str = fact.get('source_date')
        if source_date_str:
            try:
                source_date = date_parser.parse(source_date_str)
                return f"This information changed around {source_date.strftime('%B')} {source_date.year}. What was stated may have been accurate before that time."
            except Exception:
                pass
        return "This claim may have been true in the past but is no longer current."

    def detect_temporal_claim(self, claim: str) -> bool:
        temporal_keywords = ['current', 'now', 'today', 'still', 'as of', 'currently', 'presently', 'at present']
        return any(kw in claim.lower() for kw in temporal_keywords)

    def explain_outdated_claim(self, fact: Dict, verdict: str) -> str:
        if verdict != "OUTDATED" and not fact.get('was_previously_true'):
            return ""
        parts = []
        if fact.get('historical_context'):
            parts.append(fact['historical_context'])
        if fact.get('source_date'):
            parts.append(f"Information was last updated: {fact['source_date']}")
        if fact.get('was_previously_true'):
            parts.append("This claim was accurate in the past but circumstances have changed.")
        return " ".join(parts)

_historical_context_service = None

def get_historical_context_service() -> HistoricalContextService:
    global _historical_context_service
    if _historical_context_service is None:
        _historical_context_service = HistoricalContextService()
    return _historical_context_service
