#!/usr/bin/python3
"""Square class from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square from a Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate Square class.

        Args:
            size (int): size of square.
            x (int): position of x of square.
            y (int): position of y of square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size.

        Args:
            value (int): ize of Square to set.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 1:
            raise ValueError("size must be > 0")
        self.height = value
        self.width = value

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
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif n == 1:
                    self.width = arg
                elif n == 2:
                    self.x = arg
                elif n == 3:
                    self.y = arg
                n += 1
        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns to dictionary."""
        return {
            "id": self.id,
            "size": self.height,
            "x": self.x,
            "y": self.y,
        }
