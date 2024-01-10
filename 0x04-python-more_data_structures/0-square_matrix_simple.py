#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new = []
    for col in matrix:
        square = list(map(lambda x: x**2, col))
        new.append(square)
    return new
