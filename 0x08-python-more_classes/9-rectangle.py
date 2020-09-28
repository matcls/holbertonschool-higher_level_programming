#!/usr/bin/python3
"""Module to define a Rectangle."""


class Rectangle:
    """Defines a Rectangle.

    Attributes:
        number_of_instances (int): counts instance instantiation
        and deletion.
        print_symbol (any) = The symbol used for string representation.
        For default "#".
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """
        self.__class__.number_of_instances += 1
        self.width = width
        self.height = height

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

    def area(self):
        """Returns the Rectangle area."""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the Rectangle perimeter."""
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        """Returns a string representation of the
        Rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ""

        return (self.__height * ((self.__width * str(self.print_symbol)) +
                                 '\n'))[:-1]

    def __repr__(self):
        """Returns a string representation of the
        Rectangle with the # character
        to be able to recreate a new instance by using eval()"""
        return "Rectangle" + str((self.__width, self.__height))

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area.

        Args:
            rect_1 (Rectangle): First Rectangle to compare its area.
            rect_2 (rectangle): Second Rectangle to compare its area.

        Returns:
            Rectangle: The biggest rectangle based on the area.
            rect_1 if both have the same area value.

        Raises:
            TypeError: If rect_1 or rect_2 are not an instance
            of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) < Rectangle.area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Returns a Rectangle with equal width and heigh (square).

        Args:
            size (int): Square size

        Returns:
            Rectangle: A new Rectangle instance with width == height == size
        """
        return cls(size, size)
