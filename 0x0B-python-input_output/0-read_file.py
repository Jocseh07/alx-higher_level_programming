#!/usr/bin/python3
"""Function that reads a text file in UTF-8."""


def read_file(filename=""):
    """Reads a file and prints.

    Args:
        filename (str): name of the file.
    """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
