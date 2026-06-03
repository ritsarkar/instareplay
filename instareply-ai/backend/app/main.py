"""FastAPI application entrypoint for InstaReply AI."""

import logging
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
  """Create and configure the FastAPI application."""
  application = FastAPI(
    title="InstaReply AI API",
    version="0.1.0",
    description="Backend API for Instagram DM automation.",
  )

  application.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

  @application.get("/health", tags=["health"])
  async def health() -> dict[str, Any]:
    """Return service health status."""
    return {"status": "ok", "service": "instareply-ai-api"}

  @application.get("/health/db", tags=["health"])
  async def health_db() -> dict[str, Any]:
    """Return placeholder database health status for Phase 1."""
    return {"status": "pending", "detail": "Database checks are implemented in Phase 2."}

  @application.get("/health/redis", tags=["health"])
  async def health_redis() -> dict[str, Any]:
    """Return placeholder Redis health status for Phase 1."""
    return {"status": "pending", "detail": "Redis checks are implemented in Phase 5."}

  from app.routers import auth, instagram, webhook, knowledge, analytics, billing
  application.include_router(auth.router)
  application.include_router(instagram.router)
  application.include_router(webhook.router)
  application.include_router(knowledge.router)
  application.include_router(analytics.router)
  application.include_router(billing.router)

  logger.info("FastAPI application configured")
  return application

app = create_app()
