#!/usr/bin/python3
"""Function that returns true if object is subclass of class inherited."""


def inherits_from(obj, a_class):
    """Check if exactly an subclass of specified class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match obj to.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
