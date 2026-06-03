"""Instagram webhook routes."""

from fastapi import APIRouter, Request, Query, HTTPException, Response, status
import hmac
import hashlib
import json
import logging

from app.config import settings
from app.tasks.message_tasks import process_instagram_webhook

router = APIRouter(prefix="/webhook", tags=["webhook"])
logger = logging.getLogger(__name__)

@router.get("/instagram")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_challenge: int = Query(None, alias="hub.challenge"),
    hub_verify_token: str = Query(None, alias="hub.verify_token")
):
    """Verify webhook challenge from Meta."""
    if hub_mode == "subscribe" and hub_verify_token == settings.meta_webhook_verify_token:
        logger.info("Webhook verified successfully.")
        return Response(content=str(hub_challenge), media_type="text/plain")
    
    logger.warning("Failed webhook verification.")
    raise HTTPException(status_code=403, detail="Verification failed")

@router.post("/instagram")
async def receive_webhook(request: Request):
    """Receive and process incoming webhook payload from Meta."""
    # 1. Get raw body for HMAC signature verification
    raw_body = await request.body()
    signature = request.headers.get("X-Hub-Signature-256")
    
    if not signature:
        logger.warning("Received webhook without signature.")
        raise HTTPException(status_code=400, detail="Missing signature")
        
    # 2. Validate HMAC signature
    expected_signature = hmac.new(
        key=settings.meta_app_secret.encode('utf-8'),
        msg=raw_body,
        digestmod=hashlib.sha256
    ).hexdigest()
    
    expected_signature_header = f"sha256={expected_signature}"
    
    if not hmac.compare_digest(expected_signature_header, signature):
        logger.warning(f"Invalid webhook signature. Expected {expected_signature_header}, got {signature}")
        raise HTTPException(status_code=403, detail="Invalid signature")

    # 3. Parse JSON and Enqueue Task
    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    # Fast return to Meta, hand off processing to Celery
    process_instagram_webhook.delay(payload)
    
    return Response(content="EVENT_RECEIVED", status_code=status.HTTP_200_OK, media_type="text/plain")
