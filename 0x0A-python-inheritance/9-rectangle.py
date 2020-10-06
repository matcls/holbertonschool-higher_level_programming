#!/usr/bin/python3
"""Define a Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass representing a Rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle.

        Args:
            width (int): New Rectangle width.
            height (int): New Description height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the Rectangle area."""
        return self.__height * self.__width

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
