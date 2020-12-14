#!/usr/bin/python3
"""Contains the class definition of State."""

from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Define a State """
    __tablename__ = "states"
    id = Column(
        Integer,
        unique=True,
        primary_key=True,
        nullable=False
    )
    name = Column(
        String(128),
        nullable=False
    )
    cities = relationship(
        "City",
        cascade="all, delete",
        backref="state",
    )
