#!/usr/bin/python3
"""Real Definition of a rectagle"""


class Rectangle:

    """Class Definition"""

    def __init__(self, width=0, height=0):
        """Private Instance Attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
            self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
