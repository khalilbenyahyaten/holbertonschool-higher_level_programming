#!/usr/bin/python3
""" square """
Square = __import__("10-square").Square


class Square(Square):
    """ class square """
    def __str(self, size):
        return ("[Square] {}/{}".format(size, size))
