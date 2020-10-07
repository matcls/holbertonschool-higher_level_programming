#!/usr/bin/python3
"""Dictionary description with simple data structure of JSON."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}
