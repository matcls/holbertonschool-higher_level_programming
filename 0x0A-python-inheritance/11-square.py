#!/usr/bin/python3
"""Define a Square subclass of Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Subclass representing a Square."""

    def __init__(self, size):
        """Initialize a Square.

        Args:
            width (int): New Square width.
            height (int): New Square height.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the Square area."""
        return self.__size ** 2

    def __str__(self):
        """Return a text representation of Square."""
        return '[Square] {}/{}'.format(self.__size, self.__size)
