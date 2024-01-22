#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    b = 0

    while a < x:
        try:
            print("{:d}".format(my_list[a]), end="")
            b += 1
            a += 1
        except (TypeError, ValueError):
            a += 1
            print("", end="")
    print("")
    return b
