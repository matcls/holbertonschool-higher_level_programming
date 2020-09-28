#!/usr/bin/python3
"""Module to define a Rectangle."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve Rectangle width.

        Returns:
            int: Rectangle width.
        """
        return self.__width

    @property
    def height(self):
        """Retrieve Rectangle height.

        Returns:
            int: Rectangle height.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the Rectangle width.

        Args:
            value (int): Rectangle width.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the Rectangle height.

        Args:
            value (int): Rectangle height.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
