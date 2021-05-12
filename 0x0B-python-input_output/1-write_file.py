#!/usr/bin/python3
"""wrote string to txtfile UTF8 and rtrn # of char"""


def write_file(filename="", text=""):
    """function(filewritten, text wrtn)"""

    with open(filename, 'w', encoding='utf-8') as h:
        numC = h.write(text)
        return numC
