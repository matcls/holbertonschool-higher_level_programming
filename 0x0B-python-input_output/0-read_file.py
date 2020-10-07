#!/usr/bin/python3
"""Function that reads a text file."""


def read_file(filename=""):
    """Print a text file (UTF8) content to stdout."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
