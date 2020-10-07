#!/usr/bin/python3
"""Function that represent an object (Python data structure) as a string."""
import json


def from_json_string(my_str):
    """Return an Python data structure represented by a JSON string."""
    return json.loads(my_str)
