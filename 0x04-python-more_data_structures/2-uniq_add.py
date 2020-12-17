#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    s = 0
    for i in my_list:
        j = 0
        for k in new_list:
            if k == i:
                j += 1
        if j == 0:
            new_list.append(i)
            s += i
    return s
