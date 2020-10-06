#!/usr/bin/python3
"""Check if a object is inherited (directly or indirectly) of the a class."""


def inherits_from(obj, a_class):
    """Check if a object is an instance or inherited of a class.

    Args:
        obj (any): an object
        a_class (TYPE): the class to check against to.

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
