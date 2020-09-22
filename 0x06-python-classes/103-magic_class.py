#!/usr/bin/python3
"""Defines a MagicClass (circumference)."""


import math


class MagicClass:
    """Defines a MagicClass (circumference)."""

    def __init__(self, radius=0):
        """Initialize a MagicClass (circumference).

        Args:
            radius (int or float): circumference radius.
        """
        self._MagicClass__radius = 0
        if (type(radius) is not int) and (type(radius) is not float):
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Retrieve circumference area.

         Returns:
            int: the circumference area
         """
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Returns:
            int: circumference."""
        return 2 * math.pi * self._MagicClass__radius
