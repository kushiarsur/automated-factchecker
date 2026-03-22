"""
Configuration settings for the application
"""
import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# CORS settings
ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://localhost:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:3000"
]

# Model settings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
NLI_MODEL = "microsoft/deberta-v3-base"

# Verification thresholds
SIMILARITY_THRESHOLD = 0.65
CONFIDENCE_HIGH = 0.8
CONFIDENCE_MEDIUM = 0.6

# Data paths
DATA_DIR = BASE_DIR / "app" / "data"
VERIFIED_FACTS_PATH = DATA_DIR / "verified_facts.json"

# API settings
API_VERSION = "v1"
API_PREFIX = f"/api/{API_VERSION}"
