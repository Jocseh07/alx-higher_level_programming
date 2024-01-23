#!/usr/bin/python3

"""MagicClass for area and circumference."""

import math


class MagicClass:
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a circle."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area."""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Return circumference."""
        return 2 * math.pi * self.__radius
