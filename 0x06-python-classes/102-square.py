#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Square size.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve Square size.

         Returns:
            int: the Square area
         """
        return self.__size

    @size.setter
    def size(self, value):
        """sets the Square size.

        Args:
            value (int): the Square size.

        Returns:
            int: The Square size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the square area"""
        return self.__size * self.__size

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()
