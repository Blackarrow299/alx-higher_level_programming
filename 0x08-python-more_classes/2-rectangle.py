#!/usr/bin/python3

""" module composed of rectangle class """


class Rectangle:
    """ rectangle class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must >= 0")
        self.width = value

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("hight must >= 0")
        self.height = value

    def area(self):
        """ return the area of the rectangle """
        return self.width * self.height

    def perimeter(self):
        """ return perimeter of the rectangle """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
