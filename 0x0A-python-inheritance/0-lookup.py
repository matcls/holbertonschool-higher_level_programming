#!/usr/bin/python3
"""Module for lookup method."""


def lookup(obj):
    """Return the list of available attributes and methods  of an object.

    Args:
        obj (object): the object to

    Returns:
        list: methods and attributes of obj
    """
    return dir(obj)
