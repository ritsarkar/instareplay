"""Database enum values used by ORM models."""

from enum import Enum


class Plan(str, Enum):
  """Subscription plan values."""

  FREE = "free"
  STARTER = "starter"
  PRO = "pro"
  AGENCY = "agency"


class ConversationState(str, Enum):
  """Conversation lifecycle states."""

  NEW = "new"
  ACTIVE = "active"
  WAITING_FOR_HUMAN = "waiting_for_human"
  HUMAN_ACTIVE = "human_active"
  RESOLVED = "resolved"
  SNOOZED = "snoozed"


class MessageDirection(str, Enum):
  """Message direction values."""

  INBOUND = "inbound"
  OUTBOUND = "outbound"


class MessageSender(str, Enum):
  """Message sender values."""

  AI = "ai"
  HUMAN = "human"
  SYSTEM = "system"


class DeliveryStatus(str, Enum):
  """Outbound delivery status values."""

  PENDING = "pending"
  SENT = "sent"
  DELIVERED = "delivered"
  FAILED = "failed"


class KnowledgeSourceType(str, Enum):
  """Knowledge source file or entry types."""

  PDF = "pdf"
  DOCX = "docx"
  TXT = "txt"
  MANUAL = "manual"


class KnowledgeStatus(str, Enum):
  """Knowledge ingestion status values."""

  PROCESSING = "processing"
  READY = "ready"
  FAILED = "failed"


class SubscriptionStatus(str, Enum):
  """Subscription lifecycle status values."""

  ACTIVE = "active"
  CANCELLED = "cancelled"
  PAST_DUE = "past_due"
  TRIALING = "trialing"
