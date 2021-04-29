#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    H_list = []
    for h in my_list:
        if h % 2 == 0:
            H_list.append(True)
        else:
            H_list.append(False)
        return H_list
