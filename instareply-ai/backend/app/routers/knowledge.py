"""Knowledge base routes."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
import uuid

from app.database import get_db
from app.models.user import User
from app.models.knowledge_base import KnowledgeBase
from app.models.enums import KnowledgeSourceType, KnowledgeStatus
from app.middleware.auth_middleware import get_current_user
from app.tasks.knowledge_tasks import process_knowledge_document

router = APIRouter(prefix="/knowledge", tags=["knowledge"])

class KnowledgeUploadRequest(BaseModel):
    title: str
    content: str
    
class KnowledgeResponse(BaseModel):
    id: uuid.UUID
    title: str
    status: str
    chunk_count: int
    created_at: str

@router.post("/upload", status_code=status.HTTP_202_ACCEPTED)
async def upload_knowledge(
    request: KnowledgeUploadRequest,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Uploads raw text as a knowledge document and queues it for RAG processing."""
    if not request.content.strip():
        raise HTTPException(status_code=400, detail="Content cannot be empty.")
        
    doc = KnowledgeBase(
        user_id=current_user.id,
        title=request.title,
        source_type=KnowledgeSourceType.TEXT,
        raw_content=request.content,
        status=KnowledgeStatus.PROCESSING
    )
    
    db.add(doc)
    await db.commit()
    await db.refresh(doc)
    
    # Dispatch Celery task
    process_knowledge_document.delay(str(doc.id))
    
    return {"message": "Document uploaded and queued for processing", "doc_id": doc.id}

@router.get("", response_model=list[KnowledgeResponse])
async def list_knowledge(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """List all knowledge documents for the current user."""
    stmt = select(KnowledgeBase).where(KnowledgeBase.user_id == current_user.id).order_by(KnowledgeBase.created_at.desc())
    result = await db.execute(stmt)
    docs = result.scalars().all()
    
    return [
        KnowledgeResponse(
            id=d.id,
            title=d.title,
            status=d.status.value,
            chunk_count=d.chunk_count,
            created_at=d.created_at.isoformat()
        )
        for d in docs
    ]
