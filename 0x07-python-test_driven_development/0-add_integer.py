#!/usr/bin/python3
"""module for add two integers method"""


def add_integer(a, b=98):
    """Adds two integers a, b
    a and b are first casted to integers if they are float

    Args:
        a (int, float): first integer
        b (int, float): second integer, default 98

    Returns:
        int: The sum the a and b integers

    Raises:
        TypeError: if a or b are not integers or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
