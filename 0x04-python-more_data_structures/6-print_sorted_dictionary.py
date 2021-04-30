#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for h in sorted(a_dictionary):
        print('{}: {}'.format(h, a_dictionary[h]))
