"""Customer ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import Float, ForeignKey, Integer, String, UniqueConstraint, func, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Customer(Base):
  """Instagram customer profile and memory."""

  __tablename__ = "customers"
  __table_args__ = (UniqueConstraint("user_id", "ig_user_id", name="uq_customers_user_ig_user"),)

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
  ig_user_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
  name: Mapped[str | None] = mapped_column(String, nullable=True)
  username: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
  language_preference: Mapped[str] = mapped_column(String(10), nullable=False, default="en", server_default="en")
  sentiment_score: Mapped[float] = mapped_column(Float, nullable=False, default=0.5, server_default="0.5")
  total_messages: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  last_seen: Mapped[datetime | None] = mapped_column(nullable=True)
  profile_data: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict, server_default=text("'{}'::jsonb"))
  memory: Mapped[dict[str, Any]] = mapped_column(JSONB, nullable=False, default=dict, server_default=text("'{}'::jsonb"))
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

  user: Mapped["User"] = relationship("User", back_populates="customers")
  conversations: Mapped[list["Conversation"]] = relationship("Conversation", back_populates="customer", cascade="all, delete-orphan")
  messages: Mapped[list["Message"]] = relationship("Message", back_populates="customer")
