#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    B_list = my_list.copy()
    if idx < 0 or idx >=len(my_list):
        return(B_list)
    for h in range(len(B_list)):
        if h == idx:
            B_list[h] = element
            return(B_list)
