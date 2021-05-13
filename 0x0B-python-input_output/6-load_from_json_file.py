#!/usr/bin/python3
"""Loading from json"""


import json
"""module load"""


def load_from_json_file(filename):
    """funct(filename)"""

    with open(filename, encoding='utf-8') as h:
        return json.load(h)
