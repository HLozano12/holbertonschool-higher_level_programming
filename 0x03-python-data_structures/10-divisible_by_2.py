#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    h_list = []
    if my_list:
        for h in my_list:
            if h % 2 == 0:
                h_list.append(True)
            else:
                h_list.append(False)
    return (h_list)
