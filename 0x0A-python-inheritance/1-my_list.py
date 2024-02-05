#!/usr/bin/python3
"""Defines a class that inherits from list."""


class MyList(list):
    """Class that inherits from list."""

    def __init__(self):
        """Initialize the object."""
        super().__init__()

    def print_sorted(self):
        """Print the sorted list."""
        print(sorted(self))
