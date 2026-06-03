"""Token refresh celery tasks."""

import asyncio
from datetime import datetime, timedelta, timezone
from celery.utils.log import get_task_logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
import httpx

from app.database import AsyncSessionLocal
from app.models.instagram_account import InstagramAccount
from app.utils.encryption import decrypt_token, encrypt_token
from app.config import settings
from app.tasks.celery_app import celery_app

logger = get_task_logger(__name__)

async def _refresh_tokens_async():
    """Async implementation to refresh expiring tokens."""
    expiration_threshold = datetime.now(timezone.utc) + timedelta(days=7)
    
    async with AsyncSessionLocal() as session:
        # Find accounts with tokens expiring in less than 7 days
        stmt = select(InstagramAccount).where(
            InstagramAccount.is_connected == True,
            InstagramAccount.token_expires_at <= expiration_threshold
        )
        result = await session.execute(stmt)
        accounts = result.scalars().all()
        
        if not accounts:
            logger.info("No tokens require refreshing.")
            return

        async with httpx.AsyncClient() as client:
            for account in accounts:
                try:
                    decrypted_token = decrypt_token(account.access_token_encrypted)
                    # Exchange the token via Meta Graph API
                    url = f"https://graph.facebook.com/v21.0/oauth/access_token"
                    params = {
                        "grant_type": "fb_exchange_token",
                        "client_id": settings.meta_app_id,
                        "client_secret": settings.meta_app_secret,
                        "fb_exchange_token": decrypted_token,
                    }
                    response = await client.get(url, params=params)
                    
                    if response.status_code == 200:
                        data = response.json()
                        new_token = data.get("access_token")
                        expires_in = data.get("expires_in")
                        
                        if new_token:
                            account.access_token_encrypted = encrypt_token(new_token)
                            if expires_in:
                                account.token_expires_at = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
                            logger.info(f"Successfully refreshed token for account ID {account.ig_account_id}")
                    else:
                        logger.error(f"Failed to refresh token for account {account.ig_account_id}: {response.text}")
                except Exception as e:
                    logger.error(f"Error refreshing token for account {account.id}: {str(e)}")
                    
        await session.commit()

@celery_app.task
def refresh_instagram_tokens():
    """Celery task to automatically refresh expiring Instagram tokens."""
    asyncio.run(_refresh_tokens_async())
