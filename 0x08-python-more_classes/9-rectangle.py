#!/usr/bin/python3

""" module composed of rectangle class """


class Rectangle:
    """ rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.number_of_instances += 1

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

    def __str__(self) -> str:
        """return rectangle string

        Returns:
            str: string representation of rectangle
        """
        o = ""
        for i in range(0, self.height):
            for j in range(0, self.width):
                o += self.print_symbol
            if i != self.height - 1:
                o += '\n'
        return o

    def __repr__(self):
        """ Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Method that prints a message when the instance is deleted


        """
        self.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Method that returns the bigger Rectangle

        Args:
            rect_1: Rectangle 1
            rect_2: Rectangle 2

        Raises:
            TypeError: when some argument passed is not
            an instance of the Rectangle class

        Returns:
            The bigger Rectangle


        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    
    @classmethod
    def square(cls, size=0):
        """ Method that returns a new instance of Rectangle class

        Args:
            cls: rectangle class
            size: rectangle width and rectangle height

        Returns:
            a new instance of Rectangle class


        """

        return cls(size, size)