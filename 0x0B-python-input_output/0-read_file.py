#!/usr/bin/python3
"""module reads textfile(UTF8) and prints STDOUT"""


def read_file(filename=""):
    """Function(arg, no return)"""

    with open(filename, encoding='utf-8') as h:
        for line in h:
            print(line, end="")
            """like Predfined clean up Resource"""
