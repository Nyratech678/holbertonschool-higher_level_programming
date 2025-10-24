#!/usr/bin/python3
"""Model definition of a City class for SQLAlchemy."""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class definition of a City."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
