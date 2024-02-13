#!/usr/bin/python3
"""Divides all emements of a matrix."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): list of list of ints or floats.
        div (int / float): the divisor.

    """
    new = []
    str = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None or len(matrix) == 0:
        raise TypeError(str)
    if not isinstance(matrix, list):
        raise TypeError(str)
    for a in matrix:
        if not isinstance(a, list):
            raise TypeError(str)
    l = len(matrix[0])

    for a in matrix:
        for b in a:
            if type(b) not in [int, float]:
                raise TypeError(str)
        if len(a) != l:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for a in matrix:
        row = []
        for b in a:
            row.append(round(b / div, 2))
        new.append(row)
    return new
