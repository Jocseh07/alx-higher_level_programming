#!/usr/bin/python3
"""Function that appends a string to end of a file."""


def append_write(filename="", text=""):
    """Appends a string to a file.

    Args:
        filename (str): name of the file.
        text (str): text to write to string.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
