#!/usr/bin/python3
"""Given Module"""

from models.base import Base
"""Import"""


class Rectangle(Base):
    """Rect inherits child base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super()__init)__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def area(self):
        """obtain area of rect"""
        area = self.__width * self.__height
        return area

    def to_dictionary(self):
        """rtrn dict reprsnt of Rect"""
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """My setter"""
        if type(value) is not int:
            raise TypeError("width must be an interger")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        "getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        "height setter"
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueErro("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    
