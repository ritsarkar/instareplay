"""Conversation ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, Integer, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import ConversationState
from app.models.types import enum_type


class Conversation(Base):
  """Conversation between a customer and the business."""

  __tablename__ = "conversations"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
  customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, index=True)
  state: Mapped[ConversationState] = mapped_column(
    enum_type(ConversationState, "conversation_state_enum"),
    nullable=False,
    default=ConversationState.NEW,
    server_default=ConversationState.NEW.value,
  )
  last_message_at: Mapped[datetime | None] = mapped_column(nullable=True, index=True)
  message_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  ai_handled_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  human_handled_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  snoozed_until: Mapped[datetime | None] = mapped_column(nullable=True)
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

  user: Mapped["User"] = relationship("User", back_populates="conversations")
  customer: Mapped["Customer"] = relationship("Customer", back_populates="conversations")
  messages: Mapped[list["Message"]] = relationship("Message", back_populates="conversation", cascade="all, delete-orphan")
