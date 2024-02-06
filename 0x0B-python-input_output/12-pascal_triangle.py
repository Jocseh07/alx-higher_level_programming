#!/usr/bin/python3
"""Return list of integers representing Pascal Triangle."""


def pascal_triangle(n):
    """Return list of integers representing pascal triangle.

    Args:
        n (int): pascal_triangle to check.
    """
    if n <= 0:
        return []
    items = [[1]]
    while len(items) != n:
        temp = [1]
        temp2 = items[-1]

        for a in range(len(temp2) - 1):
            temp.append(temp2[a] + temp2[a + 1])

        temp.append(1)
        items.append(temp)
    return items
