#!/usr/bin/python3
""" full rectangle """
BaseGeometry = __import__("8-rectangle").Rectangle


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def area(self):
        """ area implementation """
        return self.__height * self.__width

    def __str__(self):
        """ print rectangle description """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
