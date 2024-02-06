#!/usr/bin/python3
"""Function that adds attribute to object."""


def add_attribute(obj, att, value):
    """Add new attribute to object.

    Args:
        obj(any): Object to add attribute.
        att(str): name of attribute to add.
        value(any): value of attritube.
    """
    if hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
