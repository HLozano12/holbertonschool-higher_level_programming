#!/usr/bin/python3
"""A Defined Square Class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """private instance"""
        self.__size = size

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Public Instance Method"""
        return self.__size ** 2
