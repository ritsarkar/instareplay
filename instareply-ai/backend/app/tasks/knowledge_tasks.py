"""Knowledge background tasks."""

import asyncio
import logging
from celery.utils.log import get_task_logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import uuid

from app.database import AsyncSessionLocal
from app.models.knowledge_base import KnowledgeBase
from app.models.knowledge_chunk import KnowledgeChunk
from app.models.enums import KnowledgeStatus
from app.services.rag_service import RAGService
from app.tasks.celery_app import celery_app

logger = get_task_logger(__name__)

async def _process_knowledge_document_async(kb_id_str: str):
    """Async implementation to process and embed a knowledge document."""
    kb_id = uuid.UUID(kb_id_str)
    rag_service = RAGService()

    async with AsyncSessionLocal() as session:
        # Fetch the document
        stmt = select(KnowledgeBase).where(KnowledgeBase.id == kb_id)
        result = await session.execute(stmt)
        kb_doc = result.scalars().first()
        
        if not kb_doc:
            logger.error(f"Knowledge document {kb_id} not found.")
            return
            
        try:
            # Update status to processing (just in case it was pending)
            kb_doc.status = KnowledgeStatus.PROCESSING
            await session.commit()
            
            # Chunk the raw content
            chunks = rag_service.chunk_text(kb_doc.raw_content or "")
            if not chunks:
                logger.warning(f"No chunks generated for {kb_id}.")
                kb_doc.status = KnowledgeStatus.FAILED
                await session.commit()
                return
                
            kb_doc.chunk_count = len(chunks)
            
            # Fetch embeddings
            embeddings = await rag_service.get_embeddings(chunks)
            
            # Save chunks to DB
            for idx, (chunk_text, embedding) in enumerate(zip(chunks, embeddings)):
                knowledge_chunk = KnowledgeChunk(
                    kb_id=kb_doc.id,
                    user_id=kb_doc.user_id,
                    chunk_text=chunk_text,
                    chunk_index=idx,
                    embedding=embedding
                )
                session.add(knowledge_chunk)
                
            kb_doc.status = KnowledgeStatus.READY
            await session.commit()
            logger.info(f"Successfully processed {kb_id} into {len(chunks)} chunks.")
            
        except Exception as e:
            logger.error(f"Failed to process knowledge doc {kb_id}: {str(e)}")
            await session.rollback()
            # Try to mark as failed
            try:
                kb_doc.status = KnowledgeStatus.FAILED
                await session.commit()
            except:
                pass


@celery_app.task(bind=True, max_retries=3)
def process_knowledge_document(self, kb_id_str: str):
    """
    Celery task to chunk a document, get OpenAI embeddings, 
    and store pgvector rows.
    """
    try:
        asyncio.run(_process_knowledge_document_async(kb_id_str))
    except Exception as exc:
        logger.error(f"Task process_knowledge_document failed: {exc}")
        self.retry(exc=exc, countdown=60)
