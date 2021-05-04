#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return 0
    h = 0
    for h in range(x):
        try:
            print(my_list[h], end="")
            h += 1
        except:
            break
    print('')
    return h
