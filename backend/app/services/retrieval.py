"""
Fact retrieval service using semantic search
"""
import json
import numpy as np
from typing import List, Dict, Tuple
from sentence_transformers import SentenceTransformer
import faiss
from ..config import EMBEDDING_MODEL, VERIFIED_FACTS_PATH, SIMILARITY_THRESHOLD


class FactRetriever:
    """Semantic fact retrieval using sentence embeddings and FAISS"""

    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)
        self.facts = []
        self.index = None
        self.embeddings = None
        self._load_facts()
        self._build_index()

    def _load_facts(self):
        if VERIFIED_FACTS_PATH.exists():
            with open(VERIFIED_FACTS_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.facts = data.get('facts', [])
        else:
            print(f"Warning: Verified facts file not found at {VERIFIED_FACTS_PATH}")
            self.facts = []

    def _build_index(self):
        if not self.facts:
            return
        claims = [fact['claim'] for fact in self.facts]
        self.embeddings = self.model.encode(claims, convert_to_numpy=True)
        dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(self.embeddings)

    def retrieve(self, query: str, top_k: int = 3) -> List[Tuple[Dict, float]]:
        if not self.facts or self.index is None:
            return []
        query_embedding = self.model.encode([query], convert_to_numpy=True)
        distances, indices = self.index.search(query_embedding, top_k)
        max_distance = 2.0
        similarities = 1 - (distances[0] / max_distance)
        similarities = np.clip(similarities, 0, 1)
        results = []
        for idx, sim in zip(indices[0], similarities):
            if sim >= SIMILARITY_THRESHOLD:
                fact = self.facts[idx].copy()
                results.append((fact, float(sim)))
        return results

    def get_fact_by_id(self, fact_id: str) -> Dict:
        for fact in self.facts:
            if fact.get('id') == fact_id:
                return fact
        return None


_retriever = None

def get_retriever() -> FactRetriever:
    global _retriever
    if _retriever is None:
        _retriever = FactRetriever()
    return _retriever
