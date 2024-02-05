#!/usr/bin/python3
"""Function that returns true if object is instance of class inherited."""


def is_kind_of_class(obj, a_class):
    """Check if exactly an instance of specified class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match obj to.
    """
    return isinstance(obj, a_class)
