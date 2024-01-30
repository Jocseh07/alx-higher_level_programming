#!/usr/bin/python3
"""prints a square with character #."""


def print_square(size):
    """Print square
    Args:
        size (int): size of square.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")
