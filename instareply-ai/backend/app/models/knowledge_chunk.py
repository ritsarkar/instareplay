"""Knowledge chunk ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, Integer, Text, UniqueConstraint, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base, Vector


class KnowledgeChunk(Base):
  """Vector-searchable knowledge chunk."""

  __tablename__ = "knowledge_chunks"
  __table_args__ = (UniqueConstraint("kb_id", "chunk_index", name="uq_knowledge_chunks_kb_chunk_index"),)

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  kb_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("knowledge_base.id", ondelete="CASCADE"), nullable=False, index=True)
  user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
  chunk_text: Mapped[str] = mapped_column(Text, nullable=False)
  chunk_index: Mapped[int] = mapped_column(Integer, nullable=False)
  embedding: Mapped[list[float] | None] = mapped_column(Vector(768), nullable=True)
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())

  knowledge_base: Mapped["KnowledgeBase"] = relationship("KnowledgeBase", back_populates="chunks")
  user: Mapped["User"] = relationship("User", back_populates="knowledge_chunks")
