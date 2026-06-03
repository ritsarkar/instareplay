"""Analytics routes."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func

from app.database import get_db
from app.routers.auth import get_current_user
from app.models.user import User
from app.models.customer import Customer
from app.models.knowledge import KnowledgeDocument
from app.models.conversation import Conversation
from app.models.enums import ConversationState

router = APIRouter(prefix="/analytics", tags=["analytics"])

@router.get("/")
async def get_analytics_dashboard(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    """Get aggregated analytics data for the authenticated user's dashboard."""
    
    # 1. Total Customers and Messages
    stmt = select(
        func.count(Customer.id).label("total_customers"),
        func.coalesce(func.sum(Customer.total_messages), 0).label("total_messages")
    ).where(Customer.user_id == current_user.id)
    result = await db.execute(stmt)
    row = result.first()
    total_customers = row.total_customers if row else 0
    total_messages = row.total_messages if row else 0

    # 2. Total Knowledge Documents
    stmt_docs = select(func.count(KnowledgeDocument.id)).where(KnowledgeDocument.user_id == current_user.id)
    total_docs = await db.scalar(stmt_docs) or 0

    # 3. Conversations by State
    stmt_conv = select(
        Conversation.state,
        func.count(Conversation.id).label("count")
    ).where(
        Conversation.user_id == current_user.id
    ).group_by(Conversation.state)
    
    result_conv = await db.execute(stmt_conv)
    conv_states = {state.name: count for state, count in result_conv.all()}
    
    active_conversations = conv_states.get(ConversationState.NEW.name, 0) + conv_states.get(ConversationState.ACTIVE.name, 0)
    resolved_conversations = conv_states.get(ConversationState.RESOLVED.name, 0)

    return {
        "success": True,
        "data": {
            "total_customers": total_customers,
            "total_messages_processed": total_messages,
            "total_knowledge_documents": total_docs,
            "active_conversations": active_conversations,
            "resolved_conversations": resolved_conversations
        }
    }
