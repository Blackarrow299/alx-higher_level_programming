#!/usr/bin/python3
"""
Contains the Square class, which implements a square using the Rectangle class.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that implements a square using the Rectangle class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The ID of the square.

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Gets the size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.

        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the square's attributes using either args or kwargs.

        Args:
            *args: Variable number of non-keyword arguments.
            **kwargs: Variable number of keyword arguments.

        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A formatted string representing the square.

        """
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the square.

        Returns:
            dict: A dictionary with the square's attributes.

        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
