#!/usr/bin/python3
"""Insert line of text to a fiel after each line according to string."""


def append_after(filename="", search_string="", new_string=""):
    """Append after search string.

    Args:
        search_string (str): string to search.
        new_string (str): string to append.
    """
    new = ""
    with open(filename) as f:

        for line in f:
            new += line
            if search_string in line:
                new += new_string
    with open(filename, "w") as f:
        f.write(new)
