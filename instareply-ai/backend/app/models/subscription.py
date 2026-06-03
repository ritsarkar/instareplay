"""Subscription ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, Integer, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import Plan, SubscriptionStatus
from app.models.types import enum_type


class Subscription(Base):
  """Billing subscription and usage record."""

  __tablename__ = "subscriptions"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
  plan: Mapped[Plan] = mapped_column(enum_type(Plan, "plan_enum"), nullable=False, default=Plan.FREE, server_default=Plan.FREE.value)
  status: Mapped[SubscriptionStatus] = mapped_column(
    enum_type(SubscriptionStatus, "subscription_status_enum"),
    nullable=False,
    default=SubscriptionStatus.ACTIVE,
    server_default=SubscriptionStatus.ACTIVE.value,
  )
  messages_used: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  messages_limit: Mapped[int] = mapped_column(Integer, nullable=False, default=100, server_default="100")
  current_period_start: Mapped[datetime | None] = mapped_column(nullable=True)
  current_period_end: Mapped[datetime | None] = mapped_column(nullable=True)
  razorpay_subscription_id: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
  stripe_subscription_id: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

  user: Mapped["User"] = relationship("User", back_populates="subscriptions")
