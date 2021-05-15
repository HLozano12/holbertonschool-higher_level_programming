#!/usr/bin/python3
"""Given Module"""

from models.base import Base
"""Import"""


class Rectangle(Base):
    """Rect inherits child base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super()__init__(id)
