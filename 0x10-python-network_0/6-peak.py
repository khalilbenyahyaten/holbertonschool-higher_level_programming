#!/usr/bin/python3
""" peak """
def find_peak(list_of_integers):
    if (not list_of_integers):
        return None
    elif (len(list_of_integers) == 1):
        return list_of_integers[0]
    else:
        i = list_of_integers[0]
        for j in range(1, len(list_of_integers) - 1):
            if (list_of_integers[j] >= list_of_integers[j - 1] and list_of_integers[j] >= list_of_integers[j+1]):
                i = list_of_integers[j]
                j += 1
        return i
        