#!/usr/bin/python3
"""prints a text with 2 new lines after each of these characters. ? and :"""


def text_indentation(text):
    """prints text with 2 new lines.
    Args:
        text (str): text to indent.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = 0
    found = 1
    while a < len(text):
        if found == 1 and text[a] != " ":
            found = 0
        if found == 0:
            print(text[a], end="")
            if text[a] in ".?:" and found == 0:
                print("\n")
                found = 1
        a += 1
