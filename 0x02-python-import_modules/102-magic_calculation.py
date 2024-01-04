#!/usr/bin/python3


def magic_calucation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for a in range(4, 6):
            c = add(c, a)
        return c
    else:
        return sub(a, b)
