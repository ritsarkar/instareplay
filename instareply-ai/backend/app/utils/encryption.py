"""Fernet encryption helper."""

from cryptography.fernet import Fernet
from app.config import settings
import logging

logger = logging.getLogger(__name__)

# Fallback for development if FERNET_KEY is not set. 
# DO NOT do this in production.
_key = settings.fernet_key
if not _key:
    logger.warning("FERNET_KEY is not set. Using a temporary generated key. Tokens will be lost on restart.")
    _key = Fernet.generate_key().decode()

_fernet = Fernet(_key.encode() if isinstance(_key, str) else _key)

def encrypt_token(token: str) -> str:
    """Encrypt a string token."""
    if not token:
        return ""
    return _fernet.encrypt(token.encode()).decode()

def decrypt_token(encrypted_token: str) -> str:
    """Decrypt a string token."""
    if not encrypted_token:
        return ""
    return _fernet.decrypt(encrypted_token.encode()).decode()
