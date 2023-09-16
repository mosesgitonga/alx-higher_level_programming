#!/usr/bin/python3
"""
creating city table
"""

from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import ForeignKey


class City(Base):
    """class city"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
