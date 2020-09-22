#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square.

        Args:
            size (int): Square size.
            position (int, int): Position of the Square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve Square position.

        Returns:
            tuple: Square position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set square position.

        Parameters:
            value (tuple): Position tuple value.

        Returns:
            tuple: Square position.
        """
        if (
             not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                (value[0] < 0 or value[1] < 0)
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """Calculates the Square area.

        Returns:
            int: Square area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the Square with the character #."""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.position[1]):
                    print()
            for i in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        s = ""
        if not self.__size:
            return "\n"

        if self.__position[1] > 0:
            for i in range(self.position[1]):
                s += '\n'
        for i in range(self.__size):
            for i in range(self.__position[0]):
                s += " "
            for j in range(self.__size):
                s += "#"
            s += "\n"
        s = s[:-1]
        return s
