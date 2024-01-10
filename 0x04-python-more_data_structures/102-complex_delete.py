#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    keys1 = list(a_dictionary.keys())
    for key in keys1:
        if value == a_dictionary[key]:
            del a_dictionary[key]
    return a_dictionary
