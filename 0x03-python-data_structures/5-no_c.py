#!/usr/bin/python3


def no_c(my_string):
    str = my_string
    translation = {67: None, 99: None}
    str = str.translate(translation)
    return str
