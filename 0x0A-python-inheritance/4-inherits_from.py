#!/usr/bin/python3
"""checks if an object is an instance of a class that
   inherited from the specified class"""


def inherits_from(obj, a_class):
    """ instance of a class """
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return false
