#!/usr/bin/python3
"""Check if a object is an instance or inherited of the specified class."""


def is_kind_of_class(obj, a_class):
    """Check if a object is an instance or inherited of a class.

    Args:
        obj (any): an object
        a_class (TYPE): the class to check against to.

    Returns:
        bool: Return True if the object is exactly
        an instance of the specified class; otherwise False.
    """
    return isinstance(obj, a_class)
