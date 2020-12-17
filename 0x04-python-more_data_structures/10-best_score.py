#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        x = 0
        s = ""
        for i in a_dictionary:
            if a_dictionary[i] > x:
                x = a_dictionary[i]
                s = i
        return s
    else:
        return None
