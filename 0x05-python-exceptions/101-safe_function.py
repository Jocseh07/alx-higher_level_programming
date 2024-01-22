#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        a = fct(*args)
    except Exception as e:
        a = "None"
        print("Exception: {}".format(e), file=sys.stderr)
    return a
