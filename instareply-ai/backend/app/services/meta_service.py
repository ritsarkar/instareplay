"""Meta Graph API integration service."""

import httpx
import logging
from app.config import settings

logger = logging.getLogger(__name__)

class MetaService:
    """Service for interacting with Meta Graph API endpoints."""

    def __init__(self):
        self.api_version = settings.meta_api_version
        self.base_url = f"https://graph.facebook.com/{self.api_version}"

    async def send_message(self, page_access_token: str, recipient_id: str, message_text: str) -> bool:
        """
        Sends a text message to a specific Instagram user via the Graph API.
        Returns True if successful, False otherwise.
        """
        url = f"{self.base_url}/me/messages"
        
        headers = {
            "Authorization": f"Bearer {page_access_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "recipient": {
                "id": recipient_id
            },
            "message": {
                "text": message_text
            }
        }

        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    url,
                    json=payload,
                    headers=headers,
                    timeout=15.0
                )
                response.raise_for_status()
                logger.info(f"Successfully dispatched message to Meta recipient {recipient_id}")
                return True
            except httpx.HTTPError as e:
                logger.error(f"Failed to send message via Meta API: {str(e)}")
                if hasattr(e, 'response') and e.response:
                    logger.error(f"Meta API Error Response: {e.response.text}")
                return False
