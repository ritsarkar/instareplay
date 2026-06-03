"""Reusable SQLAlchemy column type helpers."""

from enum import Enum as PyEnum
from typing import TypeVar

from sqlalchemy import Enum

EnumT = TypeVar("EnumT", bound=PyEnum)


def enum_type(enum_class: type[EnumT], name: str) -> Enum:
  """Create a SQLAlchemy enum that stores enum values instead of names."""
  return Enum(
    enum_class,
    name=name,
    values_callable=lambda members: [member.value for member in members],
  )
