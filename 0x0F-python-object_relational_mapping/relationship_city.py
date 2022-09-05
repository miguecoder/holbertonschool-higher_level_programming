#!/usr/bin/python3
"""
Definition of class City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Create attributes id, name and state_id
    like Columns with the underlying
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
