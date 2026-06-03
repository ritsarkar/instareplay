"""Database primitives for SQLAlchemy async ORM."""

from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import UserDefinedType

from app.config import settings


class Base(DeclarativeBase):
  """Base class for all ORM models."""


class Vector(UserDefinedType):
  """PostgreSQL pgvector column type."""

  cache_ok = True

  def __init__(self, dimensions: int) -> None:
    """Store the vector dimensionality for DDL compilation."""
    self.dimensions = dimensions

  def get_col_spec(self, **kwargs: object) -> str:
    """Return the PostgreSQL column specification."""
    return f"vector({self.dimensions})"


engine = create_async_engine(settings.database_url, pool_pre_ping=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
  """Yield an async database session for request-scoped dependencies."""
  async with AsyncSessionLocal() as session:
    yield session

import redis.asyncio as redis
from app.config import settings

async def get_redis() -> AsyncGenerator[redis.Redis, None]:
    client = redis.from_url(settings.upstash_redis_url, decode_responses=True)
    try:
        yield client
    finally:
        await client.aclose()
