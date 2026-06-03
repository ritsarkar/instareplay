"""Message ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Float, ForeignKey, Integer, String, Text, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import DeliveryStatus, MessageDirection, MessageSender
from app.models.types import enum_type


class Message(Base):
  """Message sent or received inside a conversation."""

  __tablename__ = "messages"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  conversation_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("conversations.id", ondelete="CASCADE"), nullable=False, index=True)
  customer_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("customers.id", ondelete="CASCADE"), nullable=False, index=True)
  content: Mapped[str] = mapped_column(Text, nullable=False)
  direction: Mapped[MessageDirection] = mapped_column(enum_type(MessageDirection, "message_direction_enum"), nullable=False)
  sent_by: Mapped[MessageSender] = mapped_column(enum_type(MessageSender, "message_sender_enum"), nullable=False)
  intent_class: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
  confidence_score: Mapped[float | None] = mapped_column(Float, nullable=True)
  delivery_status: Mapped[DeliveryStatus] = mapped_column(
    enum_type(DeliveryStatus, "delivery_status_enum"),
    nullable=False,
    default=DeliveryStatus.PENDING,
    server_default=DeliveryStatus.PENDING.value,
  )
  ig_message_id: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
  delay_applied_seconds: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  timestamp: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now(), index=True)

  conversation: Mapped["Conversation"] = relationship("Conversation", back_populates="messages")
  customer: Mapped["Customer"] = relationship("Customer", back_populates="messages")
