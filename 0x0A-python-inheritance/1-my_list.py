#!/usr/bin/python3
"""inherit from list"""


class MyList(list):
    """inherit attributes and methods from list"""
    def __init__(self):
        """instantiation of all the attributes"""
        super().__init__()

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
