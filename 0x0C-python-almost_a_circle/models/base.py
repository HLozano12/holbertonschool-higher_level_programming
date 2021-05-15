#!/usr/bin/python3
"""Our module"""

import json


class Base:
    """Class named Base"""

    __nb_objects = 0
    """private class attribute"""

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
