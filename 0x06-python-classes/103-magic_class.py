#!/usr/bin/python3
import math

"""MagicClass for area and circumference."""


class MagicClass:
    def __init__(self, radius=0):
        """Represent a circle."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area."""
        return math.pi * self.__radius**2

    def circumference(self):
        """Return circumference."""
        return math.pi * self.__radius * 2
