#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent a Rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): size of the new Rectangle.
            height (int): height of the new Rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of recangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Prints the Rectangle with #."""
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle = []
        for _ in range(self.__height):
            for _ in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")
        return "".join(rectangle)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        rectangle = "Rectangle(" + str(self.__width)
        rectangle += ", " + str(self.__height) + ")"
        return rectangle

    def __del__(self):
        """Print a message during deletion."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
