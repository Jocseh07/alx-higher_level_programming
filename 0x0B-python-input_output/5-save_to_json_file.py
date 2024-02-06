#!/usr/bin/python3
"""Writes an object to a text file, using JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to file.

    Args:
        my_obj (any): to change to JSON representation.
        filename (str): file to write.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
