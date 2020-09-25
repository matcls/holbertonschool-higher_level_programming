#!/usr/bin/python3
"""Module for divide a matrix by a int or float"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
        matrix (list):  a list of lists of integers or floats.
        div (int, floar):  divisor number

    Returns:
        list: List of lists divided matrix.

    Raises:
        TypeError: If matrix elements are not integers/floats
        TypeError: If matrix rows are not all the same size.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is zero.
    """
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    if matrix == [[]] or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i/div, 2) for i in row] for row in matrix]
