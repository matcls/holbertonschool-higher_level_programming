#!/usr/bin/python3
"""Module for class BaseGeometry."""


class BaseGeometry:
    """Define a BaseGeometry."""

    def area(self):
        """Raise an exception on call as is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if the value is integrer and raises error if not."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
