#!/usr/bin/python3
"""Define a Square class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): height and width of new Rectangle.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """For print() and str() of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "]"
        string = str(self.__width) + "/" + str(self.__height)
        return string
