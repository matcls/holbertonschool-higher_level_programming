#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            int: Square size.
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
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Returns the Square area"""
        return self.__size * self.__size

    def my_print(self):
        """Prints the Square with the character #."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
