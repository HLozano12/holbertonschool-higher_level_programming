#!/usr/bin/python3
"""Append a str at end of txtfile & rtrn char count"""


def append_write(filename="", text=""):
    """func(str, txt to appnd)"""

    with open(filename, mode='a', encoding='utf-8') as h:
        return(h.write(text))
