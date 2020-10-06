#!/usr/bin/python3
"""Module for class BaseGeometry."""


class BaseGeometry:
    """Raise an exception on call."""

    def area(self):
        """Is not implemented."""
        raise Exception("area() is not implemented")
