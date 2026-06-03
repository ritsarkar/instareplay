"""Instagram account ORM model."""

from __future__ import annotations

import uuid
from datetime import datetime

from sqlalchemy import Boolean, ForeignKey, String, Text, UniqueConstraint, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class InstagramAccount(Base):
  """Connected Instagram account for a user."""

  __tablename__ = "instagram_accounts"
  __table_args__ = (UniqueConstraint("user_id", "ig_account_id", name="uq_instagram_accounts_user_ig_account"),)

  id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
  user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
  ig_account_id: Mapped[str] = mapped_column(String, nullable=False, index=True)
  ig_username: Mapped[str | None] = mapped_column(String, nullable=True)
  business_account_id: Mapped[str | None] = mapped_column(String, nullable=True)
  page_id: Mapped[str | None] = mapped_column(String, nullable=True)
  access_token_encrypted: Mapped[str] = mapped_column(Text, nullable=False)
  token_expires_at: Mapped[datetime | None] = mapped_column(nullable=True)
  is_connected: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("false"))
  is_live: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False, server_default=text("false"))
  connected_at: Mapped[datetime | None] = mapped_column(nullable=True)
  disconnected_at: Mapped[datetime | None] = mapped_column(nullable=True)

  user: Mapped["User"] = relationship("User", back_populates="instagram_accounts")
