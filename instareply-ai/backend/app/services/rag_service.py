"""Retrieval augmented generation service."""

import httpx
import logging
import re
from typing import List
from app.config import settings

logger = logging.getLogger(__name__)

class RAGService:
    """Service for handling document chunking and vector embeddings."""
    
    def __init__(self):
        self.openai_api_key = settings.openai_api_key
        self.embedding_url = "https://api.openai.com/v1/embeddings"
        self.model = "text-embedding-3-small"
        # Project schema KnowledgeChunk specifies Vector(768)
        self.dimensions = 768
        self.chunk_size = 1000
        self.chunk_overlap = 100

    def chunk_text(self, text: str) -> List[str]:
        """
        Splits raw text into smaller overlapping chunks suitable for embeddings.
        Implements a simple recursive character splitting approach.
        """
        if not text:
            return []

        # 1. Normalize whitespace
        text = re.sub(r'\r\n', '\n', text)
        
        # 2. Split by paragraphs
        paragraphs = text.split('\n\n')
        
        chunks = []
        current_chunk = ""
        
        for p in paragraphs:
            p = p.strip()
            if not p:
                continue
                
            # If a single paragraph is too long, split by sentences
            if len(p) > self.chunk_size:
                sentences = re.split(r'(?<=[.!?]) +', p)
                for sentence in sentences:
                    if len(current_chunk) + len(sentence) > self.chunk_size and current_chunk:
                        chunks.append(current_chunk.strip())
                        # Overlap: keep the last sentence from previous chunk if possible
                        current_chunk = current_chunk.split('. ')[-1] + ". " + sentence
                    else:
                        current_chunk += " " + sentence
            else:
                if len(current_chunk) + len(p) > self.chunk_size and current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = p
                else:
                    current_chunk += "\n\n" + p if current_chunk else p
                    
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return [c for c in chunks if c]

    async def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Fetches embeddings from OpenAI for a list of text chunks.
        """
        if not texts:
            return []
            
        if not self.openai_api_key:
            logger.warning("OpenAI API key not configured. Returning empty embeddings for dev mode.")
            # Dev mock: return 0.0 vector of size 768
            return [[0.0] * self.dimensions for _ in texts]
            
        headers = {
            "Authorization": f"Bearer {self.openai_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "input": texts,
            "model": self.model,
            "dimensions": self.dimensions
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.embedding_url,
                    headers=headers,
                    json=payload,
                    timeout=30.0
                )
                response.raise_for_status()
                data = response.json()
                
                embeddings = []
                # OpenAI returns embeddings in the 'data' array, preserving input order
                for item in sorted(data.get("data", []), key=lambda x: x["index"]):
                    embeddings.append(item["embedding"])
                    
                return embeddings
            except httpx.HTTPError as e:
                logger.error(f"Error fetching embeddings from OpenAI: {str(e)}")
                raise
