#!/usr/bin/python3
"""Contains class definition of State and instance Base."""
from relationship_state_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """Class with id and name and inherits from Base."""

    __tablename__ = "cities"

    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
