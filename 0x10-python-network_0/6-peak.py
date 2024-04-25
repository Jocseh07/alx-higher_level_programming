#!/usr/bin/python3
"""Find a peak in list of unsorted integers."""


def find_peak(list_of_integers):
    """Find a pick in list of integers."""
    if list_of_integers is None or list_of_integers == []:
        return None
    bottom = 0
    top = len(list_of_integers)
    middle = (top - bottom) // 2
    if top == 1:
        return list_of_integers[0]
    if top == 2:
        if list_of_integers[0] > list_of_integers[1]:
            return list_of_integers[0]
        else:
            return list_of_integers[1]
    if list_of_integers[middle] >= list_of_integers[middle + 1] and \
             list_of_integers[middle] >= list_of_integers[middle - 1]:
        return list_of_integers[middle]
    if list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
    if list_of_integers[middle] < list_of_integers[middle - 1]:
        return find_peak(list_of_integers[:middle])
