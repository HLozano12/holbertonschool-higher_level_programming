#!/usr/bin/python3
"""Our Module"""


def inherits_from(obj, a_class):
    """our Prototype to inherit direct or indirectly"""

    return issubclass(type(obj), a_class) and type(obj) is not a_class
"""If a_class is inherited, will be true"""
