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
