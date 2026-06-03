"""Authentication schemas."""

from pydantic import BaseModel, EmailStr, Field
import uuid

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    password: str = Field(..., min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class GoogleToken(BaseModel):
    token: str

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    plan: str
    onboarding_step: int

    class Config:
        from_attributes = True
