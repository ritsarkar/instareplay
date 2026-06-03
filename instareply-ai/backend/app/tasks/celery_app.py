"""Celery application configuration."""

import os
from celery import Celery
from app.config import settings

celery_app = Celery(
    "instareply_tasks",
    broker=settings.upstash_redis_url,
    backend=settings.upstash_redis_url,
    include=[
        "app.tasks.token_refresh_tasks",
        "app.tasks.message_tasks",
        "app.tasks.notification_tasks",
        "app.tasks.knowledge_tasks",
    ]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_time_limit=3600,
)

# Optional: Add beat schedule if periodic token refresh is needed
celery_app.conf.beat_schedule = {
    "refresh-instagram-tokens-daily": {
        "task": "app.tasks.token_refresh_tasks.refresh_instagram_tokens",
        "schedule": 86400.0, # Every 24 hours
    }
}
