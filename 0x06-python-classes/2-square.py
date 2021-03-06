#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            int: Square size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
