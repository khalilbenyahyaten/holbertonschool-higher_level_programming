#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    for j in range(x, 0):
        try:
            print("{}".format(my_list[j]), end="")
        except:
            pass
    print("")
    return j
