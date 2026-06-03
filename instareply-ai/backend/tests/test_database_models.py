"""Database model metadata tests."""

import app.models
from app.database import Base, Vector


def test_all_phase_two_tables_are_registered() -> None:
  """Verify SQLAlchemy metadata contains the Phase 2 schema tables."""
  expected_tables = {
    "users",
    "instagram_accounts",
    "conversations",
    "customers",
    "messages",
    "knowledge_base",
    "knowledge_chunks",
    "subscriptions",
    "audit_logs",
  }

  assert set(Base.metadata.tables) == expected_tables


def test_knowledge_chunk_embedding_uses_pgvector_dimensions() -> None:
  """Verify knowledge chunk embeddings are configured for Gemini dimensions."""
  embedding_column = Base.metadata.tables["knowledge_chunks"].columns["embedding"]

  assert isinstance(embedding_column.type, Vector)
  assert embedding_column.type.dimensions == 768


def test_models_package_import_is_used() -> None:
  """Keep the app.models import visible to linters and static checks."""
  assert app.models.__all__
