#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represts a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): size of new square.
            position (int, int): tuple containing position.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position.
        Args:
            value(int): position of the Square.
        """
        str = "position must be a tuple of 2 positive integers"
        if (not isinstance(value, tuple)) or len(value) != 2:
            raise TypeError(str)
        for num in value:
            if (not isinstance(num, int)) or num < 0:
                raise TypeError(str)
        self.__position = value

    def area(self):
        """Find the area of the Square."""
        return self.__size * self.__size

    def my_print(self):
        """Prints in stdout the square with the character #."""
        if self.__size == 0:
            print("")
            return

        [print("") for _ in range(0, self.__position[1])]
        for _ in range(0, self.__size):
            [print(" ", end="") for _ in range(0, self.__position[0])]
            [print("#", end="") for _ in range(0, self.__size)]
            print("")
