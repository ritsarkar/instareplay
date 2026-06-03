"""Instagram integration service."""

import httpx
from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
import urllib.parse

from app.config import settings
from app.models.instagram_account import InstagramAccount
from app.models.user import User
from app.utils.encryption import encrypt_token

def get_auth_url() -> str:
    """Generate the Meta OAuth URL."""
    redirect_uri = f"{settings.frontend_url}/onboarding" # In a real app, you might have a dedicated callback route on frontend
    
    # We will use a backend redirect URI for simplicity of the flow in Phase 4.
    redirect_uri = f"{settings.frontend_url}/api/auth/callback/instagram"
    
    # Using the standard backend callback
    # We don't have a frontend domain configured for api routes right now, so we will use the backend directly.
    # The requirement says: GET /instagram/callback -> handle OAuth, store token
    
    backend_redirect_uri = "http://localhost:8000/instagram/callback"
    
    scopes = [
        "instagram_basic",
        "instagram_manage_messages",
        "pages_manage_metadata",
        "pages_read_engagement",
        "pages_show_list"
    ]
    
    params = {
        "client_id": settings.meta_app_id,
        "redirect_uri": backend_redirect_uri,
        "scope": ",".join(scopes),
        "response_type": "code",
    }
    
    url = f"https://www.facebook.com/{settings.meta_api_version}/dialog/oauth?" + urllib.parse.urlencode(params)
    return url

async def handle_callback(code: str, user_id: str, db: AsyncSession) -> InstagramAccount:
    """Exchange OAuth code for tokens and fetch account details."""
    backend_redirect_uri = "http://localhost:8000/instagram/callback"
    
    async with httpx.AsyncClient() as client:
        # 1. Exchange code for short-lived token
        token_url = f"https://graph.facebook.com/{settings.meta_api_version}/oauth/access_token"
        token_params = {
            "client_id": settings.meta_app_id,
            "client_secret": settings.meta_app_secret,
            "redirect_uri": backend_redirect_uri,
            "code": code,
        }
        token_res = await client.get(token_url, params=token_params)
        if token_res.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to exchange code for token")
            
        short_token = token_res.json().get("access_token")
        
        # 2. Exchange for long-lived token
        ll_params = {
            "grant_type": "fb_exchange_token",
            "client_id": settings.meta_app_id,
            "client_secret": settings.meta_app_secret,
            "fb_exchange_token": short_token,
        }
        ll_res = await client.get(token_url, params=ll_params)
        
        if ll_res.status_code != 200:
            long_token = short_token
            expires_in = 3600
        else:
            long_token = ll_res.json().get("access_token")
            expires_in = ll_res.json().get("expires_in", 5184000) # Default to 60 days
            
        # 3. Get user pages
        pages_url = f"https://graph.facebook.com/{settings.meta_api_version}/me/accounts"
        pages_res = await client.get(pages_url, params={"access_token": long_token})
        
        if pages_res.status_code != 200 or not pages_res.json().get("data"):
            raise HTTPException(status_code=400, detail="No Facebook pages found for this user")
            
        # Try to find a page with an Instagram business account
        ig_account_id = None
        ig_username = None
        page_id = None
        
        for page in pages_res.json().get("data", []):
            p_id = page.get("id")
            p_token = page.get("access_token")
            
            ig_url = f"https://graph.facebook.com/{settings.meta_api_version}/{p_id}"
            ig_params = {
                "fields": "instagram_business_account",
                "access_token": p_token
            }
            ig_res = await client.get(ig_url, params=ig_params)
            
            if ig_res.status_code == 200:
                ig_data = ig_res.json().get("instagram_business_account")
                if ig_data:
                    ig_account_id = ig_data.get("id")
                    page_id = p_id
                    
                    # Optional: Get IG username
                    profile_url = f"https://graph.facebook.com/{settings.meta_api_version}/{ig_account_id}"
                    profile_res = await client.get(profile_url, params={"fields": "username", "access_token": p_token})
                    if profile_res.status_code == 200:
                        ig_username = profile_res.json().get("username")
                        
                    break
                    
        if not ig_account_id:
            raise HTTPException(status_code=400, detail="No Instagram Business Account linked to your Facebook pages.")
            
        # 4. Save to DB
        stmt = select(InstagramAccount).where(InstagramAccount.user_id == user_id)
        result = await db.execute(stmt)
        account = result.scalars().first()
        
        encrypted_token = encrypt_token(long_token)
        expiry = datetime.now(timezone.utc) + timedelta(seconds=expires_in)
        
        if account:
            account.ig_account_id = ig_account_id
            account.ig_username = ig_username
            account.page_id = page_id
            account.access_token_encrypted = encrypted_token
            account.token_expires_at = expiry
            account.is_connected = True
            account.connected_at = datetime.now(timezone.utc)
            account.disconnected_at = None
        else:
            account = InstagramAccount(
                user_id=user_id,
                ig_account_id=ig_account_id,
                ig_username=ig_username,
                page_id=page_id,
                access_token_encrypted=encrypted_token,
                token_expires_at=expiry,
                is_connected=True,
                connected_at=datetime.now(timezone.utc)
            )
            db.add(account)
            
        await db.commit()
        await db.refresh(account)
        return account

async def disconnect_account(user_id: str, db: AsyncSession) -> None:
    stmt = select(InstagramAccount).where(InstagramAccount.user_id == user_id)
    result = await db.execute(stmt)
    account = result.scalars().first()
    
    if account:
        account.is_connected = False
        account.disconnected_at = datetime.now(timezone.utc)
        await db.commit()
