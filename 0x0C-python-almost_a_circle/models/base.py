#!/usr/bin/python3
"""Base class."""
import csv
import json


class Base:
    """Base class.

    Args:
        __nb_objects (int): nb instantiated bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiate a class.

        Args:
            id (int): id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to return JSON string representation

        Args:
            list_dictionaries (list): list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes json representation to file.

        Args:
            list_objs (list): list.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dictionaries = [a.to_dictionary() for a in list_objs]
                f.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Return list of JSON string representation."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return instance with all atributes set.

        Args:
            dictionary (dictionary): dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**a) for a in list_dictionaries]

        except:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves to csv file.

        Args:
            list_objs (list): list.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is None:
                writer = csv.writer(f)
                if cls.__name__ == "Rectangle":
                    writer.writerow(["id", "width", "height", "x", "y"])
                else:
                    writer.writerow(["id", "size", "x", "y"])
                for a in list_objs:
                    writer.writerow(a.to_dictionary())

    @classmethod
    def load_from_file_csv(cls, list_objs):
        """Loads from csv file.

        Args:
            list_objs (list): list.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                if list_objs is None:
                    return []
                list_dictionaries = Base.from_json_string(csv.reader(f))
                return [cls.create(**a) for a in list_dictionaries]

        except:
            return []
