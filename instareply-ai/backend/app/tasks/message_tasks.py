"""Message processing task."""

import asyncio
import logging
from celery.utils.log import get_task_logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime, timezone

from app.database import AsyncSessionLocal
from app.models.instagram_account import InstagramAccount
from app.models.customer import Customer
from app.models.conversation import Conversation
from app.models.message import Message
from app.models.enums import MessageDirection, MessageSender, ConversationState, DeliveryStatus
from app.services.ai_service import AIService
from app.services.meta_service import MetaService
from cryptography.fernet import Fernet
from app.config import settings
from app.tasks.celery_app import celery_app

logger = get_task_logger(__name__)

async def _process_webhook_async(payload: dict):
    """Async implementation to parse Meta webhook payloads."""
    object_type = payload.get("object")
    if object_type != "instagram":
        logger.warning(f"Ignored non-instagram webhook object: {object_type}")
        return

    async with AsyncSessionLocal() as session:
        for entry in payload.get("entry", []):
            # Page ID or IG Account ID (Meta usually sends the page ID here or IG account ID depending on webhook subscription)
            for messaging in entry.get("messaging", []):
                sender_id = messaging.get("sender", {}).get("id")
                recipient_id = messaging.get("recipient", {}).get("id")
                message_data = messaging.get("message", {})
                
                # We only process text messages for now
                if not message_data or not message_data.get("text"):
                    continue
                    
                message_text = message_data.get("text")
                message_mid = message_data.get("mid")
                
                # 1. Find the connected Instagram Account
                # The recipient_id is the IG account ID in inbound messages
                stmt = select(InstagramAccount).where(InstagramAccount.ig_account_id == recipient_id, InstagramAccount.is_connected == True)
                result = await session.execute(stmt)
                account = result.scalars().first()
                
                if not account:
                    logger.error(f"Received webhook for unknown or disconnected IG account: {recipient_id}")
                    continue
                    
                user_id = account.user_id

                # 2. Get or create Customer
                stmt = select(Customer).where(Customer.ig_user_id == sender_id, Customer.user_id == user_id)
                result = await session.execute(stmt)
                customer = result.scalars().first()
                
                if not customer:
                    customer = Customer(
                        user_id=user_id,
                        ig_user_id=sender_id,
                        total_messages=0
                    )
                    session.add(customer)
                    await session.flush() # flush to get customer.id
                    
                customer.last_seen = datetime.now(timezone.utc)
                customer.total_messages += 1

                # 3. Get or create active Conversation
                stmt = select(Conversation).where(
                    Conversation.customer_id == customer.id,
                    Conversation.user_id == user_id,
                ).order_by(Conversation.created_at.desc()).limit(1)
                
                result = await session.execute(stmt)
                conversation = result.scalars().first()
                
                # If no conversation or it was closed (e.g. state == RESOLVED) more than 24h ago, create new one.
                # For simplicity, we just check if one exists or create a new one.
                if not conversation or conversation.state == ConversationState.RESOLVED:
                    conversation = Conversation(
                        user_id=user_id,
                        customer_id=customer.id,
                        state=ConversationState.NEW,
                        message_count=0
                    )
                    session.add(conversation)
                    await session.flush()

                conversation.last_message_at = datetime.now(timezone.utc)
                conversation.message_count += 1
                
                # 4. Save the Message
                new_message = Message(
                    conversation_id=conversation.id,
                    customer_id=customer.id,
                    content=message_text,
                    direction=MessageDirection.INBOUND,
                    sent_by=MessageSender.CUSTOMER,
                    ig_message_id=message_mid,
                    delivery_status=DeliveryStatus.DELIVERED
                )
                session.add(new_message)
                
                logger.info(f"Processed message {message_mid} from {sender_id} to {recipient_id}")
                
                # 5. Generate AI Reply
                ai_service = AIService()
                ai_response = await ai_service.generate_reply(
                    db=session,
                    message_text=message_text,
                    user_id=user_id,
                    conversation_id=conversation.id
                )
                
                # Save the AI response as a pending outbound message
                outbound_message = Message(
                    conversation_id=conversation.id,
                    customer_id=customer.id,
                    content=ai_response,
                    direction=MessageDirection.OUTBOUND,
                    sent_by=MessageSender.AI,
                    delivery_status=DeliveryStatus.PENDING
                )
                session.add(outbound_message)
                await session.flush()
                
                # 6. Send the message via Meta API
                logger.info(f"Generated AI response for conversation {conversation.id}. Dispatching to Meta...")
                
                try:
                    f = Fernet(settings.fernet_key.encode())
                    decrypted_token = f.decrypt(account.access_token.encode()).decode()
                    
                    meta_service = MetaService()
                    success = await meta_service.send_message(
                        page_access_token=decrypted_token,
                        recipient_id=customer.ig_user_id,
                        message_text=ai_response
                    )
                    
                    if success:
                        outbound_message.delivery_status = DeliveryStatus.DELIVERED
                    else:
                        outbound_message.delivery_status = DeliveryStatus.FAILED
                        
                except Exception as e:
                    logger.error(f"Failed to decrypt token or send message: {str(e)}")
                    outbound_message.delivery_status = DeliveryStatus.FAILED
                
        await session.commit()

@celery_app.task
def process_instagram_webhook(payload: dict):
    """Celery task to handle incoming Instagram Webhooks asynchronously."""
    asyncio.run(_process_webhook_async(payload))
