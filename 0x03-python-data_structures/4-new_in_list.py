#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or len(my_list) - 1 < idx:
        return my_list
    copy = my_list.copy()
    copy[idx] = element
    return copy
