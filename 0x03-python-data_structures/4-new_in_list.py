#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    l = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return l
    else:
        l[idx] = element
        return l
