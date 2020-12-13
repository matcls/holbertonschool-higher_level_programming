#!/usr/bin/python3
"""Base model of a City."""

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from model_state import (
    Base,
    State
)


class City(Base):
    """Represent a citie.

    Attributes:
        id (sqlalchemy.Int): City id.
        name (sqlalchemy.str): City name.
    """
    __tablename__ = "cities"
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
    state_id = Column(
        Integer,
        ForeignKey(State.id),
        nullable=False
    )
