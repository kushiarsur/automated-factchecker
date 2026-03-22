"""
Trusted source lookup service
"""
from typing import Optional, Dict, List

TRUSTED_SOURCES = {
    "factcheck_org": "https://www.factcheck.org/api/",
    "snopes": "https://www.snopes.com/api/",
    "politifact": "https://www.politifact.com/api/",
    "reuters_factcheck": "https://www.reuters.com/fact-check/api/",
    "who": "https://www.who.int/api/",
    "cdc": "https://www.cdc.gov/api/"
}

class TrustedSourceLookup:
    def __init__(self):
        self.sources = TRUSTED_SOURCES
        self.enabled = False

    async def lookup_claim(self, claim: str, category: Optional[str] = None) -> Optional[Dict]:
        # TODO: Implement actual API calls when keys are available
        return None

    async def search_recent_claims(self, keywords: List[str], days: int = 30) -> List[Dict]:
        return []

    def get_source_credibility(self, source_name: str) -> float:
        known_credible_sources = {
            "WHO": 0.98, "CDC": 0.97, "Reuters": 0.95,
            "FactCheck.org": 0.94, "Snopes": 0.92,
            "PolitiFact": 0.91, "NASA": 0.98, "NIH": 0.97
        }
        return known_credible_sources.get(source_name, 0.7)

_lookup_service = None

def get_lookup_service() -> TrustedSourceLookup:
    global _lookup_service
    if _lookup_service is None:
        _lookup_service = TrustedSourceLookup()
    return _lookup_service
