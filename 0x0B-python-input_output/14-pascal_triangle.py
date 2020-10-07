#!/usr/bin/python3
"""Rrepresents the Pascal’s triangle of n with a list of integers."""


def pascal_triangle(n):
    """Return a list of list of integers representing a Pascal triangle."""
    triangle = [[1 for i in range(row + 1)] for row in range(n)]
    for n in range(n):
        for j in range(n - 1):
            triangle[n][j + 1] = sum(triangle[n - 1][j:j + 2])
    return triangle
