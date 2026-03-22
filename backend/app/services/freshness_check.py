"""
Freshness checking service
"""
from datetime import datetime, timedelta
from typing import Dict, Tuple, Optional
from dateutil import parser as date_parser

class FreshnessChecker:
    FRESHNESS_WINDOWS = {
        "politics": timedelta(days=90),
        "business": timedelta(days=180),
        "technology": timedelta(days=365),
        "health": timedelta(days=180),
        "science": timedelta(days=730),
        "sports": timedelta(days=30),
        "general": timedelta(days=365)
    }

    TIME_SENSITIVE_KEYWORDS = [
        'current', 'now', 'today', 'recently', 'latest',
        'as of', 'this year', 'ceo', 'president', 'leader',
        'price', 'cost', 'rate', 'stock', 'market'
    ]

    def check_freshness(self, fact: Dict, category: Optional[str] = None) -> Tuple[bool, Optional[str]]:
        source_date_str = fact.get('source_date')
        if not source_date_str:
            return True, None
        try:
            source_date = date_parser.parse(source_date_str)
        except Exception:
            return True, None

        category = category or fact.get('category', 'general')
        freshness_window = self.FRESHNESS_WINDOWS.get(category, self.FRESHNESS_WINDOWS['general'])
        age = datetime.now() - source_date

        if age > freshness_window:
            months_old = age.days // 30
            return False, f"Information is {months_old} months old and may be outdated for {category} content"
        return True, None

    def is_time_sensitive_claim(self, claim: str) -> bool:
        return any(kw in claim.lower() for kw in self.TIME_SENSITIVE_KEYWORDS)

    def requires_live_lookup(self, claim: str, fact: Optional[Dict] = None) -> bool:
        if not fact:
            return self.is_time_sensitive_claim(claim)
        is_fresh, _ = self.check_freshness(fact)
        if not is_fresh:
            return True
        if self.is_time_sensitive_claim(claim):
            fact_claim = fact.get('claim', '').lower()
            if not any(kw in fact_claim for kw in self.TIME_SENSITIVE_KEYWORDS[:5]):
                return True
        return False

_freshness_checker = None

def get_freshness_checker() -> FreshnessChecker:
    global _freshness_checker
    if _freshness_checker is None:
        _freshness_checker = FreshnessChecker()
    return _freshness_checker
