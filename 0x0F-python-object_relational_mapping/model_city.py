#!/usr/bin/python3
"""Base model of a City."""

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)
from model_state import Base
from model_state import State


class City(Base):
    """Represent a city.

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
        ForeignKey("states.id"),
        nullable=False
    )
