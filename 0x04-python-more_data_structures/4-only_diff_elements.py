#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    h = set(set_1)
    l = set(set_2)
    return (h ^ l)
