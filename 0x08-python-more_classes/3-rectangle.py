#!/usr/bin/python3
"""Real Definition of a rectagle"""


class Rectangle:

    """Class Definition"""

    def __init__(self, width=0, height=0):
        """Private Instance Attributes"""
        self.width = width
        self.height = height

    def __str__(self):
        """prints Rectangle w/ char"""
        RectStr = ""
        if self.__height == 0 or self.__width == 0:
            return RectStr
        for h in range(0, self.__height):
            for l in range(0, self.__width):
                RectStr += '#'
            if h < self.__height - 1:
                RectStr += "\n"
        return (RectStr)

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2
