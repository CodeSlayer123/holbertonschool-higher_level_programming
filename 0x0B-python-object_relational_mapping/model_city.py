#!/usr/bin/python3
"""contains class named city"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """class City that contains table named cities"""
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
