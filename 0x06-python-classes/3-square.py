#!/usr/bin/python3
"""define a square class"""


class Square:
    """square class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        a = self.__size * self.__size
        return a
