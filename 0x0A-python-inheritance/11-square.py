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
