#!/usr/bin/python3
"""Lazy multiplication with NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of 2 matrices.

    Args:
        m_a (list of list of ints or floats): first matrix
        m_b (list of list of ints or floats): second matrix
    """
    return np.matmul(m_a, m_b)
