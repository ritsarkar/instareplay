"""Knowledge base ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, Integer, String, Text, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import KnowledgeSourceType, KnowledgeStatus
from app.models.types import enum_type


class KnowledgeBase(Base):
  """Uploaded or manual knowledge document."""

  __tablename__ = "knowledge_base"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
  title: Mapped[str] = mapped_column(String(255), nullable=False)
  source_type: Mapped[KnowledgeSourceType] = mapped_column(enum_type(KnowledgeSourceType, "knowledge_source_type_enum"), nullable=False)
  raw_content: Mapped[str | None] = mapped_column(Text, nullable=True)
  chunk_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
  status: Mapped[KnowledgeStatus] = mapped_column(
    enum_type(KnowledgeStatus, "knowledge_status_enum"),
    nullable=False,
    default=KnowledgeStatus.PROCESSING,
    server_default=KnowledgeStatus.PROCESSING.value,
  )
  is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("true"))
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

  user: Mapped["User"] = relationship("User", back_populates="knowledge_documents")
  chunks: Mapped[list["KnowledgeChunk"]] = relationship("KnowledgeChunk", back_populates="knowledge_base", cascade="all, delete-orphan")
