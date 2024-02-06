#!/usr/bin/python3
"""Function that returns JSON representation of an object(string)."""
import json


def to_json_string(myobj):
    """Return JSON representation.

    Args:
        myobj (str): object to change to JSON.
    """
    return json.dumps(myobj)
