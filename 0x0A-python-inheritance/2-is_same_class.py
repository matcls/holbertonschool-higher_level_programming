#!/usr/bin/python3
"""Check if a object is is exactly an instance of the specified class."""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class.

    Args:
        obj (any): an object
        a_class (type): the class to check against to.

    Returns:
        bool: Return True if the object is exactly
        an instance of the specified class; otherwise False.
    """
    return type(obj) is a_class
