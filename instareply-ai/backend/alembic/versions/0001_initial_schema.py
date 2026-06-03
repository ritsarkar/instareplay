"""Create initial application schema.

Revision ID: 0001_initial_schema
Revises: None
Create Date: 2026-06-03
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from sqlalchemy.types import UserDefinedType

revision: str = "0001_initial_schema"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


class Vector(UserDefinedType):
  """PostgreSQL pgvector column type for migrations."""

  cache_ok = True

  def __init__(self, dimensions: int) -> None:
    """Store the vector dimensionality for DDL compilation."""
    self.dimensions = dimensions

  def get_col_spec(self, **kwargs: object) -> str:
    """Return the PostgreSQL column specification."""
    return f"vector({self.dimensions})"


plan_enum = postgresql.ENUM("free", "starter", "pro", "agency", name="plan_enum", create_type=False)
conversation_state_enum = postgresql.ENUM(
  "new",
  "active",
  "waiting_for_human",
  "human_active",
  "resolved",
  "snoozed",
  name="conversation_state_enum",
  create_type=False,
)
message_direction_enum = postgresql.ENUM("inbound", "outbound", name="message_direction_enum", create_type=False)
message_sender_enum = postgresql.ENUM("ai", "human", "system", name="message_sender_enum", create_type=False)
delivery_status_enum = postgresql.ENUM("pending", "sent", "delivered", "failed", name="delivery_status_enum", create_type=False)
knowledge_source_type_enum = postgresql.ENUM("pdf", "docx", "txt", "manual", name="knowledge_source_type_enum", create_type=False)
knowledge_status_enum = postgresql.ENUM("processing", "ready", "failed", name="knowledge_status_enum", create_type=False)
subscription_status_enum = postgresql.ENUM(
  "active",
  "cancelled",
  "past_due",
  "trialing",
  name="subscription_status_enum",
  create_type=False,
)


def create_enums() -> None:
  """Create PostgreSQL enum types used by the schema."""
  bind = op.get_bind()
  for enum_type in (
    plan_enum,
    conversation_state_enum,
    message_direction_enum,
    message_sender_enum,
    delivery_status_enum,
    knowledge_source_type_enum,
    knowledge_status_enum,
    subscription_status_enum,
  ):
    enum_type.create(bind, checkfirst=True)


def drop_enums() -> None:
  """Drop PostgreSQL enum types used by the schema."""
  bind = op.get_bind()
  for enum_type in (
    subscription_status_enum,
    knowledge_status_enum,
    knowledge_source_type_enum,
    delivery_status_enum,
    message_sender_enum,
    message_direction_enum,
    conversation_state_enum,
    plan_enum,
  ):
    enum_type.drop(bind, checkfirst=True)


def upgrade() -> None:
  """Apply the initial schema migration."""
  op.execute(sa.text("CREATE EXTENSION IF NOT EXISTS pgcrypto"))
  op.execute(sa.text("CREATE EXTENSION IF NOT EXISTS vector"))
  create_enums()

  op.create_table(
    "users",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("name", sa.String(length=255), nullable=False),
    sa.Column("email", sa.String(length=255), nullable=False),
    sa.Column("hashed_password", sa.String(), nullable=True),
    sa.Column("google_id", sa.String(), nullable=True),
    sa.Column("plan", plan_enum, server_default="free", nullable=False),
    sa.Column("onboarding_step", sa.Integer(), server_default="1", nullable=False),
    sa.Column("is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.Column("updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("email"),
  )
  op.create_index("ix_users_email", "users", ["email"], unique=False)
  op.create_index("ix_users_google_id", "users", ["google_id"], unique=False)

  op.create_table(
    "instagram_accounts",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("ig_account_id", sa.String(), nullable=False),
    sa.Column("ig_username", sa.String(), nullable=True),
    sa.Column("business_account_id", sa.String(), nullable=True),
    sa.Column("page_id", sa.String(), nullable=True),
    sa.Column("access_token_encrypted", sa.Text(), nullable=False),
    sa.Column("token_expires_at", sa.DateTime(), nullable=True),
    sa.Column("is_connected", sa.Boolean(), server_default=sa.text("false"), nullable=False),
    sa.Column("is_live", sa.Boolean(), server_default=sa.text("false"), nullable=False),
    sa.Column("connected_at", sa.DateTime(), nullable=True),
    sa.Column("disconnected_at", sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("user_id", "ig_account_id", name="uq_instagram_accounts_user_ig_account"),
  )
  op.create_index("ix_instagram_accounts_ig_account_id", "instagram_accounts", ["ig_account_id"], unique=False)
  op.create_index("ix_instagram_accounts_user_id", "instagram_accounts", ["user_id"], unique=False)

  op.create_table(
    "customers",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("ig_user_id", sa.String(), nullable=False),
    sa.Column("name", sa.String(), nullable=True),
    sa.Column("username", sa.String(), nullable=True),
    sa.Column("language_preference", sa.String(length=10), server_default="en", nullable=False),
    sa.Column("sentiment_score", sa.Float(), server_default="0.5", nullable=False),
    sa.Column("total_messages", sa.Integer(), server_default="0", nullable=False),
    sa.Column("last_seen", sa.DateTime(), nullable=True),
    sa.Column("profile_data", postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column("memory", postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("user_id", "ig_user_id", name="uq_customers_user_ig_user"),
  )
  op.create_index("ix_customers_ig_user_id", "customers", ["ig_user_id"], unique=False)
  op.create_index("ix_customers_user_id", "customers", ["user_id"], unique=False)
  op.create_index("ix_customers_username", "customers", ["username"], unique=False)

  op.create_table(
    "conversations",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("customer_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("state", conversation_state_enum, server_default="new", nullable=False),
    sa.Column("last_message_at", sa.DateTime(), nullable=True),
    sa.Column("message_count", sa.Integer(), server_default="0", nullable=False),
    sa.Column("ai_handled_count", sa.Integer(), server_default="0", nullable=False),
    sa.Column("human_handled_count", sa.Integer(), server_default="0", nullable=False),
    sa.Column("snoozed_until", sa.DateTime(), nullable=True),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["customer_id"], ["customers.id"], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
  )
  op.create_index("ix_conversations_customer_id", "conversations", ["customer_id"], unique=False)
  op.create_index("ix_conversations_last_message_at", "conversations", ["last_message_at"], unique=False)
  op.create_index("ix_conversations_user_id", "conversations", ["user_id"], unique=False)

  op.create_table(
    "messages",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("conversation_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("customer_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("content", sa.Text(), nullable=False),
    sa.Column("direction", message_direction_enum, nullable=False),
    sa.Column("sent_by", message_sender_enum, nullable=False),
    sa.Column("intent_class", sa.String(), nullable=True),
    sa.Column("confidence_score", sa.Float(), nullable=True),
    sa.Column("delivery_status", delivery_status_enum, server_default="pending", nullable=False),
    sa.Column("ig_message_id", sa.String(), nullable=True),
    sa.Column("delay_applied_seconds", sa.Integer(), server_default="0", nullable=False),
    sa.Column("timestamp", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["conversation_id"], ["conversations.id"], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(["customer_id"], ["customers.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
  )
  op.create_index("ix_messages_conversation_id", "messages", ["conversation_id"], unique=False)
  op.create_index("ix_messages_customer_id", "messages", ["customer_id"], unique=False)
  op.create_index("ix_messages_ig_message_id", "messages", ["ig_message_id"], unique=False)
  op.create_index("ix_messages_intent_class", "messages", ["intent_class"], unique=False)
  op.create_index("ix_messages_timestamp", "messages", ["timestamp"], unique=False)

  op.create_table(
    "knowledge_base",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("title", sa.String(length=255), nullable=False),
    sa.Column("source_type", knowledge_source_type_enum, nullable=False),
    sa.Column("raw_content", sa.Text(), nullable=True),
    sa.Column("chunk_count", sa.Integer(), server_default="0", nullable=False),
    sa.Column("status", knowledge_status_enum, server_default="processing", nullable=False),
    sa.Column("is_active", sa.Boolean(), server_default=sa.text("true"), nullable=False),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
  )
  op.create_index("ix_knowledge_base_user_id", "knowledge_base", ["user_id"], unique=False)

  op.create_table(
    "knowledge_chunks",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("kb_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("chunk_text", sa.Text(), nullable=False),
    sa.Column("chunk_index", sa.Integer(), nullable=False),
    sa.Column("embedding", Vector(768), nullable=True),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["kb_id"], ["knowledge_base.id"], ondelete="CASCADE"),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
    sa.UniqueConstraint("kb_id", "chunk_index", name="uq_knowledge_chunks_kb_chunk_index"),
  )
  op.create_index("ix_knowledge_chunks_kb_id", "knowledge_chunks", ["kb_id"], unique=False)
  op.create_index("ix_knowledge_chunks_user_id", "knowledge_chunks", ["user_id"], unique=False)

  op.create_table(
    "subscriptions",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column("plan", plan_enum, server_default="free", nullable=False),
    sa.Column("status", subscription_status_enum, server_default="active", nullable=False),
    sa.Column("messages_used", sa.Integer(), server_default="0", nullable=False),
    sa.Column("messages_limit", sa.Integer(), server_default="100", nullable=False),
    sa.Column("current_period_start", sa.DateTime(), nullable=True),
    sa.Column("current_period_end", sa.DateTime(), nullable=True),
    sa.Column("razorpay_subscription_id", sa.String(), nullable=True),
    sa.Column("stripe_subscription_id", sa.String(), nullable=True),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    sa.PrimaryKeyConstraint("id"),
  )
  op.create_index("ix_subscriptions_razorpay_subscription_id", "subscriptions", ["razorpay_subscription_id"], unique=False)
  op.create_index("ix_subscriptions_stripe_subscription_id", "subscriptions", ["stripe_subscription_id"], unique=False)
  op.create_index("ix_subscriptions_user_id", "subscriptions", ["user_id"], unique=False)

  op.create_table(
    "audit_logs",
    sa.Column("id", postgresql.UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
    sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column("action", sa.String(length=100), nullable=False),
    sa.Column("entity_type", sa.String(length=50), nullable=True),
    sa.Column("entity_id", postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column("metadata", postgresql.JSONB(astext_type=sa.Text()), server_default=sa.text("'{}'::jsonb"), nullable=False),
    sa.Column("ip_address", sa.String(), nullable=True),
    sa.Column("created_at", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
    sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="SET NULL"),
    sa.PrimaryKeyConstraint("id"),
  )
  op.create_index("ix_audit_logs_action", "audit_logs", ["action"], unique=False)
  op.create_index("ix_audit_logs_created_at", "audit_logs", ["created_at"], unique=False)
  op.create_index("ix_audit_logs_entity_id", "audit_logs", ["entity_id"], unique=False)
  op.create_index("ix_audit_logs_entity_type", "audit_logs", ["entity_type"], unique=False)
  op.create_index("ix_audit_logs_user_id", "audit_logs", ["user_id"], unique=False)


def downgrade() -> None:
  """Rollback the initial schema migration."""
  op.drop_index("ix_audit_logs_user_id", table_name="audit_logs")
  op.drop_index("ix_audit_logs_entity_type", table_name="audit_logs")
  op.drop_index("ix_audit_logs_entity_id", table_name="audit_logs")
  op.drop_index("ix_audit_logs_created_at", table_name="audit_logs")
  op.drop_index("ix_audit_logs_action", table_name="audit_logs")
  op.drop_table("audit_logs")

  op.drop_index("ix_subscriptions_user_id", table_name="subscriptions")
  op.drop_index("ix_subscriptions_stripe_subscription_id", table_name="subscriptions")
  op.drop_index("ix_subscriptions_razorpay_subscription_id", table_name="subscriptions")
  op.drop_table("subscriptions")

  op.drop_index("ix_knowledge_chunks_user_id", table_name="knowledge_chunks")
  op.drop_index("ix_knowledge_chunks_kb_id", table_name="knowledge_chunks")
  op.drop_table("knowledge_chunks")

  op.drop_index("ix_knowledge_base_user_id", table_name="knowledge_base")
  op.drop_table("knowledge_base")

  op.drop_index("ix_messages_timestamp", table_name="messages")
  op.drop_index("ix_messages_intent_class", table_name="messages")
  op.drop_index("ix_messages_ig_message_id", table_name="messages")
  op.drop_index("ix_messages_customer_id", table_name="messages")
  op.drop_index("ix_messages_conversation_id", table_name="messages")
  op.drop_table("messages")

  op.drop_index("ix_conversations_user_id", table_name="conversations")
  op.drop_index("ix_conversations_last_message_at", table_name="conversations")
  op.drop_index("ix_conversations_customer_id", table_name="conversations")
  op.drop_table("conversations")

  op.drop_index("ix_customers_username", table_name="customers")
  op.drop_index("ix_customers_user_id", table_name="customers")
  op.drop_index("ix_customers_ig_user_id", table_name="customers")
  op.drop_table("customers")

  op.drop_index("ix_instagram_accounts_user_id", table_name="instagram_accounts")
  op.drop_index("ix_instagram_accounts_ig_account_id", table_name="instagram_accounts")
  op.drop_table("instagram_accounts")

  op.drop_index("ix_users_google_id", table_name="users")
  op.drop_index("ix_users_email", table_name="users")
  op.drop_table("users")

  drop_enums()
