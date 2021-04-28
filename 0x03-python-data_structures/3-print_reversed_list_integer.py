#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        h_list = my_list.copy()
        h_list.reverse()
        for h in range(len(h_list)):
            print("{:d}".format(h_list[h]))
