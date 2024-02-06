#!/usr/bin/python3
"""Function that writes string to a text file and returns chars written."""


def write_file(filename="", text=""):
    """Writes a string to a file.

    Args:
        filename (str): name of the file.
        text (str): text to write to string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return f.write(text)
