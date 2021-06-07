#!/usr/bin/python3
"""Our Module provided"""


def add_integer(a, b=98):
    """Our provided prototype to add 2 ints

    """


    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return a + b