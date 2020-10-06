#!/usr/bin/python3
"""This module inherits from list."""


class MyList(list):
    """Print sorted (ascending sort) list."""

    def print_sorted(self):
        """Print a sorted (ascending sort) list."""
        print(sorted(self))
