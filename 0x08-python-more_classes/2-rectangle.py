#!/usr/bin/python3

""" module composed of rectangle class """


class Rectangle:
    """ rectangle class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width of rectangle

        Returns:
            intger: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width of the rectangle

        Args:
            value (int): width

        Raises:
            TypeError: width must be integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be integer")
        elif value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @property
    def height(self):
        """return height of rectangle

        Returns:
            intger: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height of the rectangle

        Args:
            value (int): height

        Raises:
            TypeError: height must be integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be integer")
        elif value < 0:
            raise ValueError("height must >= 0")
        self.__height = value

    def area(self):
        """return area of  the rectangle

        Returns:
            int: area
        """
        return self.width * self.height

    def perimeter(self):
        """reeturn perimiter of the rectangle

        Returns:
            int: permiter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2
