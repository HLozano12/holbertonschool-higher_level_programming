#!/usr/bin/python3
"""Our module"""

import json
import os


class Base:
    """Class named Base"""

    __nb_objects = 0
    """private class attribute"""

    def __init__(self, id=None):

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_onjects

    @staticmethod
    def to_json_string(list_dictionaries):
        """update class Base"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "{}"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """return list of json rep"""
        if json_string is None or json_string == '':
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write json str rep to list_obj"""
        if list_objs is None:
            list_objs = []
        j_string = []
        for obj in list_objs:
            j_string.append(obj.to_dictionary())
        j_string = cls.to_json_string(j_string)
        with open(cls.__name__ + ".json", mode='w') as h:
            h.write(json_string)

    @classmethod
    def load_from_file(cls):
        """method to return list of instances"""
        the_list = []
        obj_list = []
        filename = cls.__name__ + ".json"
        if os.path.exists(filename):
            with open(filename, mode="r") as file:
                json_str = file.read()
            the_list = cls.from_json_string(json_str)
            for idx in the_list:
                webster = dict(item)
                obj = cls.create(**my_dict)
                obj_list.append(obj)
            return obj_list
        else:
            return the_list

    @classmethod
    def create(cls, **dictionary):
        """return an instance with attr set"""
        if len(dictionary) == 1:
            dummy = cls(1)
            dummy.update(**dictionary)
        else:
            dummy = cls(2, 2)
            dummy.update(**dictionary)
        return dummy
