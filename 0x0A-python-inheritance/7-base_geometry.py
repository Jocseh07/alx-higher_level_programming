#!/usr/bin/python3
"""Base Geometry class."""


class BaseGeometry:
    """Define base geometry class."""

    def area(self):
        """Area of base geometry."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate the value.

        Args:
            name (str): name of parameter.
            value (int): value of parameter.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
