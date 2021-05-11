#!/usr/bin/python3
"""Our Module"""


class MyList(list):
    """inherent the list"""

    def print_sorted(self):
        """Our Prototype that prints list sorted"""

        print(sorted(self))
