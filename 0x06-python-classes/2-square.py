#!/usr/bin/python3
"""define a square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise Exception
        except TypeError:
            print('size must be an integer')
        except (ValueError, Exception):
            print('size must be >= 0')
