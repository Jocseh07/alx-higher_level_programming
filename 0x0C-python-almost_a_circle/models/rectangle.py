#!/usr/bin/python3
"""Define a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Rectangle class from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiate a Rectangle class.

        Args:
            width (int): width of Rectangle.
            height (int): height of Rectangle.
            x (int): x.
            y (int): y.
        """
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @height.setter
    def height(self, value):
        """Setter for height.

        Args:
            value (int): height of Rectangle to set.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 1:
            raise ValueError("height must be > 0")
        self.__height = value

    @width.setter
    def width(self, value):
        """Setter for width.

        Args:
            value (int): width of Rectangle to set.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 1:
            raise ValueError("width must be > 0")
        self.__width = value

    @x.setter
    def x(self, value):
        """Setter for x.

        Args:
            value (int): position of x to set.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter for y.

        Args:
            value (int): position of y to set.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of rectangle."""
        return self.width * self.height

    def display(self):
        """Prints out Rectangle with #."""
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for _ in range(self.y)]
        for _ in range(self.height):
            [print(" ", end="") for _ in range(self.x)]
            [print("#", end="") for _ in range(self.width)]
            print("")

    def __str__(self):
        """Override str."""
        str = "[{}]".format(self.__class__.__name__)
        str += " ({}) {}/{}".format(self.id, self.x, self.y)
        str += " - {}/{}".format(self.width, self.height)
        return str

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            args (int): new values to update.
            kwargs (int): key value pairs to update.
        """
        if args and len(args) != 0:
            n = 0
            for arg in args:
                if n == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.height = arg
                elif n == 3:
                    self.x = arg
                elif n == 4:
                    self.y = arg
                n += 1
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns to dictionary."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y,
        }
