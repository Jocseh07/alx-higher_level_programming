#!/usr/bin/python3
"""Function that returns the dictionary decription with simple structure."""


def class_to_json(obj):
    """Return dictionary description with simple structure.

    Args:
        obj (class): instance of a class.
    """
    return obj.__dict__
