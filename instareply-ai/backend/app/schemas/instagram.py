"""Instagram schemas."""

from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class InstagramAccountResponse(BaseModel):
    id: uuid.UUID
    ig_account_id: str
    ig_username: Optional[str] = None
    is_connected: bool
    is_live: bool
    connected_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class ConnectResponse(BaseModel):
    url: str

class CallbackRequest(BaseModel):
    code: str

class StatusResponse(BaseModel):
    is_connected: bool
    account: Optional[InstagramAccountResponse] = None
