#!/usr/bin/python3
""" read file """


def read_file(filename=""):
    """ read utf-8 file """
    with open(filename, "r", encoding="utf-8") as a:
        print(a.read(), end="")
