#!/usr/bin/python3
"""
model_state.py - defines a class `State` and an instance
`Base` of declarative_base from SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String
from model_base import Base


class State(Base):
    """State class inherits from Base"""

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', String(128), nullable=False)

