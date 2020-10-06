#!/usr/bin/python3
"""Module for add attribute method."""


def add_attribute(obj, attr, val):
    """Add a new attribute to an object if it’s possible."""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")
