#!/usr/bin/python3
"""Student class."""


class Student:
    """Student instance."""

    def __init__(self, first_name, last_name, age):
        """Initialize class.

        Args:
            first_name (str): first name.
            last_name (str): last name.
            age (int): age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of Student instance.

        Args:
            attrs (list): list of strings.
        """
        if type(attrs) == list:
            if all(type(a) == str for a in attrs):
                return {k: getattr(self, k) for k in attrs}
        return self.__dict__
