"""Authentication routes."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Annotated
import redis.asyncio as redis
import uuid

from app.database import get_db, get_redis
from app.models.user import User
from app.schemas.auth import UserCreate, UserLogin, Token, GoogleToken, UserResponse
from app.services.auth_service import (
    verify_password, get_password_hash, create_access_token, create_refresh_token, verify_google_token
)
from app.middleware.auth_middleware import get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=Token)
async def signup(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    stmt = select(User).where(User.email == user_in.email)
    result = await db.execute(stmt)
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user_in.password)
    user = User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=hashed_password
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    
    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: AsyncSession = Depends(get_db)
):
    stmt = select(User).where(User.email == form_data.username)
    result = await db.execute(stmt)
    user = result.scalars().first()
    if not user or not user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    
    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
        
    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/google", response_model=Token)
async def google_auth(token_in: GoogleToken, db: AsyncSession = Depends(get_db)):
    idinfo = verify_google_token(token_in.token)
    if not idinfo:
        raise HTTPException(status_code=400, detail="Invalid Google token")
    
    email = idinfo.get("email")
    name = idinfo.get("name")
    google_id = idinfo.get("sub")
    
    if not email:
        raise HTTPException(status_code=400, detail="Email not provided by Google")
        
    stmt = select(User).where(User.email == email)
    result = await db.execute(stmt)
    user = result.scalars().first()
    
    if not user:
        user = User(
            name=name,
            email=email,
            google_id=google_id
        )
        db.add(user)
        await db.commit()
        await db.refresh(user)
    elif not user.google_id:
        user.google_id = google_id
        await db.commit()
        
    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

@router.post("/refresh", response_model=Token)
async def refresh_token(
    refresh_token: str,
    db: AsyncSession = Depends(get_db),
    redis_client: redis.Redis = Depends(get_redis)
):
    from app.config import settings
    import jwt
    
    # Check if token is blacklisted
    is_blacklisted = await redis_client.get(f"bl_{refresh_token}")
    if is_blacklisted:
        raise HTTPException(status_code=401, detail="Token has been revoked")
        
    try:
        payload = jwt.decode(refresh_token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        user_id = payload.get("sub")
        token_type = payload.get("type")
        if user_id is None or token_type != "refresh":
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
        
    stmt = select(User).where(User.id == user_id)
    result = await db.execute(stmt)
    user = result.scalars().first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
        
    access_token = create_access_token(data={"sub": str(user.id)})
    new_refresh_token = create_refresh_token(data={"sub": str(user.id)})
    
    # Blacklist old refresh token
    exp = payload.get("exp")
    import time
    ttl = int(exp - time.time())
    if ttl > 0:
        await redis_client.setex(f"bl_{refresh_token}", ttl, "1")
        
    return {"access_token": access_token, "refresh_token": new_refresh_token, "token_type": "bearer"}

@router.post("/logout")
async def logout(
    current_user: Annotated[User, Depends(get_current_user)],
    token: str = Depends(OAuth2PasswordBearer(tokenUrl="auth/login")),
    redis_client: redis.Redis = Depends(get_redis)
):
    from app.config import settings
    import jwt
    import time
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
        exp = payload.get("exp")
        ttl = int(exp - time.time())
        if ttl > 0:
            await redis_client.setex(f"bl_{token}", ttl, "1")
    except jwt.InvalidTokenError:
        pass
    return {"detail": "Successfully logged out"}

@router.get("/me", response_model=UserResponse)
async def get_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user
