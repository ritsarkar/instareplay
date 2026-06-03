"""User ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, Integer, String, func, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.enums import Plan
from app.models.types import enum_type


class User(Base):
  """Application user and business owner."""

  __tablename__ = "users"

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  name: Mapped[str] = mapped_column(String(255), nullable=False)
  email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
  hashed_password: Mapped[str | None] = mapped_column(String, nullable=True)
  google_id: Mapped[str | None] = mapped_column(String, nullable=True, index=True)
  plan: Mapped[Plan] = mapped_column(enum_type(Plan, "plan_enum"), nullable=False, default=Plan.FREE, server_default=Plan.FREE.value)
  onboarding_step: Mapped[int] = mapped_column(Integer, nullable=False, default=1, server_default="1")
  is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True, server_default=text("true"))
  created_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(nullable=False, server_default=func.now(), onupdate=func.now())

  instagram_accounts: Mapped[list["InstagramAccount"]] = relationship("InstagramAccount", back_populates="user", cascade="all, delete-orphan")
  customers: Mapped[list["Customer"]] = relationship("Customer", back_populates="user", cascade="all, delete-orphan")
  conversations: Mapped[list["Conversation"]] = relationship("Conversation", back_populates="user", cascade="all, delete-orphan")
  knowledge_documents: Mapped[list["KnowledgeBase"]] = relationship("KnowledgeBase", back_populates="user", cascade="all, delete-orphan")
  knowledge_chunks: Mapped[list["KnowledgeChunk"]] = relationship("KnowledgeChunk", back_populates="user", cascade="all, delete-orphan")
  subscriptions: Mapped[list["Subscription"]] = relationship("Subscription", back_populates="user", cascade="all, delete-orphan")
  audit_logs: Mapped[list["AuditLog"]] = relationship("AuditLog", back_populates="user")
