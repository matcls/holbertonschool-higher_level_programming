#!/usr/bin/python3
"""Multiplies two matrices using Numpy module"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (matrix): Description
        m_b (matrix): Description

    Returns:
        matrix: multiplication of m_a and m_b.
    """
    return numpy.matmul(m_a, m_b)
