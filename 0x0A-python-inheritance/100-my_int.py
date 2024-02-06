#!/usr/bin/python3
"""Class that inherits from int."""


class MyInt(int):
    """Inverts == and !=."""

    def __eq__(self, value):
        """set == to !="""
        return self != value

    def __ne__(self, value):
        """set != to =="""
        return self == value
