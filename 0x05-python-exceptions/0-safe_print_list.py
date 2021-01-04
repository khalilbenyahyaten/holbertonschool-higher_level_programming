#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    k = 0
    j = 0
    for j in range(0, x):
        try:
            print("{}".format(my_list[j]), end="")
            k += 1
        except:
            pass
    print("")
    return k
