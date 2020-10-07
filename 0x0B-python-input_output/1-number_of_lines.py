#!/usr/bin/python3
"""Function that returns the number of lines of a text file."""


def number_of_lines(filename=""):
    """Return the number of lines of a text file."""
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())
