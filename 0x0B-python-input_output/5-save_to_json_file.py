#!/usr/bin/python3
"""module to write an obj to txtfile using json rep"""


import json


def save_to_json_file(my_obj, filename):
    """Func(arg, filename)"""

    with open(filename, mode='w', encoding='utf-8') as h:
        return json.dump(my_obj, h)
