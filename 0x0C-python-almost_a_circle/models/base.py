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
        j_string_list = []
        for obj in list_objs:
            j_string_list.append(obj.to_dictionary())
        json_string = cls.to__json_string(j_string_list)
        with open(cls.__name__ + ".json", mode='w') as h:
            h.write(json_string)

    @classmethod
    def load_from_file(cls):
        """method to return list of instances"""
        filename = cls.__name__ + ".json"
        if not os.path.exists(file_path):
            return []
        else:
            with open(file_path), 'r') as h:
                 list = cls.from_json_string(h.read())
            list_rect = []
            for rect in list:
                list_rect.append(cls.create(**rect))
        return list_rect

    @classmethod
    def create(cls, **dictionary):
        """return an instance with attr set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1)
            dummy.update(**dictionary)
        if:
            dummy = cls(2, 2)
            dummy.update(**dictionary)
        return dummy
