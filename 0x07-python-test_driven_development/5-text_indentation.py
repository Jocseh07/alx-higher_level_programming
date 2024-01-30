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
    while a < len(text):
        print(text[a], end="")
        if text[a] in ".?:":
            print("\n")
        a += 1
