#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represts a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): size of new square.
        """
        self.__size = size

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
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Find the area of the Square."""
        return self.__size**2

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")
        for _ in range(0, self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print("")
