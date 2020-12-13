#!/usr/bin/python3
"""Base model of a state and an instance Base = declarative_base()."""

from sqlalchemy import (
    Column,
    String,
    Integer
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a state.

    Attributes:
        id (sqlalchemy.Int): State id.
        name (sqlalchemy.str): State name.
    """
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
        unique=True,
        nullable=False,
        primary_key=True
    )
    name = Column(
        String(128),
        nullable=False
    )
