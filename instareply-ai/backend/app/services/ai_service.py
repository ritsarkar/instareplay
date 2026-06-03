"""AI orchestration service."""

import httpx
import logging
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.config import settings
from app.models.knowledge_chunk import KnowledgeChunk
from app.models.message import Message
from app.services.rag_service import RAGService

logger = logging.getLogger(__name__)

class AIService:
    """Service for handling RAG context retrieval and Gemini generation."""
    
    def __init__(self):
        self.gemini_api_key = settings.gemini_api_key
        self.gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.gemini_api_key}"
        self.rag_service = RAGService()

    async def retrieve_context(self, db: AsyncSession, text: str, user_id: uuid.UUID) -> str:
        """Embeds the query and fetches the top 3 most relevant knowledge chunks."""
        try:
            # 1. Get embedding for the query
            embeddings = await self.rag_service.get_embeddings([text])
            if not embeddings or not embeddings[0]:
                return ""
            query_embedding = embeddings[0]
            
            # 2. Vector search using pgvector `<=>` (cosine distance)
            # We want the chunks closest to our query embedding for this specific user.
            stmt = select(KnowledgeChunk).where(
                KnowledgeChunk.user_id == user_id
            ).order_by(
                KnowledgeChunk.embedding.cosine_distance(query_embedding)
            ).limit(3)
            
            result = await db.execute(stmt)
            chunks = result.scalars().all()
            
            if not chunks:
                return ""
                
            # Combine the chunks into a single context string
            context = "\n\n---\n\n".join([chunk.chunk_text for chunk in chunks])
            return context
            
        except Exception as e:
            logger.error(f"Failed to retrieve context: {str(e)}")
            return ""

    async def generate_reply(self, db: AsyncSession, message_text: str, user_id: uuid.UUID, conversation_id: uuid.UUID) -> str:
        """
        Retrieves context, formats prompt, and calls Gemini to generate a response.
        """
        if not self.gemini_api_key:
            logger.warning("Gemini API key not configured. Returning fallback response.")
            return "Thank you for your message! Our team will get back to you shortly."

        # 1. Get RAG Context
        context = await self.retrieve_context(db, message_text, user_id)
        
        # 2. Get Chat History (last 5 messages)
        stmt = select(Message).where(
            Message.conversation_id == conversation_id
        ).order_by(Message.timestamp.desc()).limit(5)
        
        result = await db.execute(stmt)
        recent_messages = result.scalars().all()
        # Reverse to get chronological order
        recent_messages.reverse()
        
        history_text = ""
        for msg in recent_messages:
            sender = "User" if msg.sent_by.value == "CUSTOMER" else "AI"
            history_text += f"{sender}: {msg.content}\n"
            
        # 3. Construct Prompt
        system_instruction = (
            "You are InstaReply AI, a helpful, professional, and concise customer support assistant. "
            "Your goal is to answer the user's question based strictly on the provided Knowledge Base Context. "
            "If the context does not contain the answer, politely state that you do not know and a human agent will assist them. "
            "Do NOT make up information."
        )
        
        prompt = f"""
Knowledge Base Context:
{context if context else 'No relevant knowledge found.'}

Recent Conversation History:
{history_text if history_text else 'No prior history.'}

User's Latest Message: {message_text}

Generate a concise and helpful reply:
"""
        
        # 4. Call Gemini API
        payload = {
            "system_instruction": {
                "parts": [{"text": system_instruction}]
            },
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.3,
                "maxOutputTokens": 500
            }
        }
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    self.gemini_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                    timeout=20.0
                )
                response.raise_for_status()
                data = response.json()
                
                # Extract text from Gemini response
                candidates = data.get("candidates", [])
                if candidates and candidates[0].get("content", {}).get("parts", []):
                    return candidates[0]["content"]["parts"][0].get("text", "").strip()
                else:
                    return "Sorry, I couldn't process your request right now."
                    
            except httpx.HTTPError as e:
                logger.error(f"Gemini API Error: {str(e)}")
                return "Our AI is currently experiencing delays. A human will be with you shortly."
