#!/usr/bin/python3
"""
python file that contains the class definition of a State
and an instance Base = declarative_base()
State class that inherits from Base
Links to MySQL Table States
Class atty id to rep auto gen, uniq int, cannot be null and is pk
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Module comment for class inherit"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True, nullable=True)
    name = Column(String(128), nullable=False)
