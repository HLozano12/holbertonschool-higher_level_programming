#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    webster = a_dictionary.copy()
    for h in webster:
        if webster[h] is value:
            del a_dictionary[h]
    return a_dictionary
