#!/usr/bin/python3
""" peak"""
def find_peak(list_of_integers):
    if list_of_integers == []:
        return None
    s = len(list_of_integers)
    if s == 1:
        return list_of_integers[0]
    elif s == 2:
        return max(list_of_integers)
    half = int(s / 2)
    p = list_of_integers[half]
    if p > list_of_integers[half + 1] and p > list_of_integers[half - 1]:
        return p
    elif p < list_of_integers[half + 1]:
        return find_peak(list_of_integers[half + 1:])
    else:
        return find_peak(list_of_integers[:half])
        