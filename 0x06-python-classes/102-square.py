#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represts a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size.
        Args:
            value(int): size of the Square.
        """
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be an number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Find the area of the Square."""
        return self.__size**2

    def __eq__(self, other):
        """Define == comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define != comparison."""
        return self.area() != other.area()

    def __ge__(self, other):
        """Define >= comparison."""
        return self.area() >= other.area()

    def __le__(self, other):
        """Define <= comparison."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define > comparison."""
        return self.area() > other.area()

    def __lt__(self, other):
        """Define < comparison."""
        return self.area() < other.area()
