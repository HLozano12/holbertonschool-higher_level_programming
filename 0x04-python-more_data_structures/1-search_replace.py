#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ninja = my_list[:]
    l = 0
    for trtl in ninja:
        if trtl == search:
            ninja[l] = replace
        l += 1
    return ninja
