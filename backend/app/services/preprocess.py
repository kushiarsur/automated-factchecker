"""
Text preprocessing service
"""
import re

def clean_text(text: str) -> str:
    """Clean and normalize input text"""
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'#(\w+)', r'\1', text)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'[^\w\s\.,!?-]', '', text)
    text = ' '.join(text.split())
    return text.strip()

def normalize_claim(claim: str) -> str:
    """Normalize claim for better matching"""
    claim = claim.lower()
    claim = clean_text(claim)
    fillers = ['just', 'really', 'very', 'actually', 'literally']
    for filler in fillers:
        claim = re.sub(r'\b' + filler + r'\b', '', claim, flags=re.IGNORECASE)
    return ' '.join(claim.split())
