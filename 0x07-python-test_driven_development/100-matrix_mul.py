#!/usr/bin/python3
"""Module for multiply two matrix.
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrix.

    Args:
        m_a: first matrix
        m_b: second matrix

    Returns:
        matrix: a new matrix from m_a * m_b

    Raises:
        Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangle.
        ValueError: If m_a or m_b can not be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[] for i in range(len(m_a))]

    for row in m_a:
        for col in m_b[0]:
            count = 0
            for i in m_b:
                count += m_a[row][i] * m_b[i][col]
            new_matrix[row].append(count)

    return new_matrix
