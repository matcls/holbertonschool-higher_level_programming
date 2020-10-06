#!/usr/bin/python3
"""Module for a class MyInt that inherits from int."""


class MyInt(int):
    """Inverts equal an different operators."""

    def __eq__(self, other):
        """= is !=."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """!= is =."""
        return int.__eq__(self, other)
