#!/usr/bin/python3
"""A Defined Square Class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """instantiation w/ optional size"""
        self.__size = size

        if isinstance(size, int) is not True:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
