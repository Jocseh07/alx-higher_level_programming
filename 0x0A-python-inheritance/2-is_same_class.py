#!/usr/bin/python3
"""Function that checks if object is instance of specified class."""


def is_same_class(obj, a_class):
    """Check if exactly an instance of specified class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match obj to.
    """
    return type(obj) == a_class
