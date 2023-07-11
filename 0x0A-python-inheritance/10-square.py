#!/usr/bin/python3
"""
    10-square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
        Square  inherits from Rectangle
    """

    def __init__(self, size):
        """
            initialises Square
        """
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """
            Returns the area of square
        """
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format("Rectangle", self.__size, self.__size))
