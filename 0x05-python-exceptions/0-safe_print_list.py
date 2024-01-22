#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    b = 0

    while a < x:
        try:
            print("{}".format(my_list[a]), end="")
            b += 1
            a += 1
        except IndexError:
            a += 1
            print("", end="")
    print("")
    return b
