#!/usr/bin/python3
"""Our Module"""


class BaseGeometry:
    """Our class"""
    def area(self):

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance to validate value"""
        if type(value) is not int:
            """IF not int"""
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
