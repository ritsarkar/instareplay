"""Audit log ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime
from typing import Any

from sqlalchemy import ForeignKey, String, func, text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class AuditLog(Base):
  """Audit trail entry for sensitive actions and task failures."""

  __tablename__ = "audit_logs"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True, index=True)
  action: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
  entity_type: Mapped[str | None] = mapped_column(String(50), nullable=True, index=True)
  entity_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True, index=True)
  metadata_: Mapped[dict[str, Any]] = mapped_column("metadata", JSONB, nullable=False, default=dict, server_default=text("'{}'::jsonb"))
  ip_address: Mapped[str | None] = mapped_column(String, nullable=True)
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now(), index=True)

  user: Mapped["User | None"] = relationship("User", back_populates="audit_logs")
