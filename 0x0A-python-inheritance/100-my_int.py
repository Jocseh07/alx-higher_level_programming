#!/usr/bin/python3
"""Class that inherits from int."""


class MyInt(int):
    """Inverts == and !=."""

    def __eq__(self, value):
        """set == to !="""
        return not type(value) == int

    def __ne__(self, value):
        """set != to =="""
        return not type(value) != int
