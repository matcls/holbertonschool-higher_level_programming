#!/usr/bin/python3
"""Contains the class definition of City."""

from relationship_city import Base
from relationship_city import City
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


class State(Base):
    """Define a State """
    __tablename__ = "states"
    id = Column(
        Integer,
        autoincrement=True,
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
        cascade="all,delete",
        backref="state",
    )
