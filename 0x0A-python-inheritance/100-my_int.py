#!/usr/bin/python3
""" inherit from int """


class MyInt(int):
    """ myint class """
    def __eq__(self, i):
        """ equal """
        return not super().__eq__(i)

    def __ne__(self, i):
        """ myint class """
        return not super().__ne__(i)
