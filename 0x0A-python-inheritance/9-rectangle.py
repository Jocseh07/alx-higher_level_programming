#!/usr/bin/python3
"""Rectangle class."""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class which inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): width of new Rectangle.
            height (int): height of new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Get the area."""
        return self.__height * self.__width

    def __str__(self):
        """For print() and str() of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "]"
        string = str(self.__width) + "/" + str(self.__height)
        return string
