#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    x = 0
    for i in range(0, len(my_list) - 1):
        if my_list[i] > x:
            x = my_list[i]
    return x
