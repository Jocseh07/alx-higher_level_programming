#!/usr/bin/python3
"""multipies 2 matrices."""


def matrix_mul(m_a, m_b):
    """Returns multiple of 2 matrices.

    Args:
        m_a (list): matrix list of lists
        m_b (list): matrix list of lists
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    str = " should contain only integers or floats"
    for row in m_a:
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError("m_a{}".format(str))
    for row in m_b:
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError("m_b{}".format(str))

    l = len(m_a[0])
    for row in m_a:
        if len(row) != l:
            raise TypeError("each row of m_a must be of the same size")

    l = len(m_b[0])
    for row in m_b:
        if len(row) != l:
            raise TypeError("each row of m_b must be of the same size")

    inverted = []
    for a in range(len(m_b[0])):
        add = []
        for b in range(len(m_b)):
            add.append(m_b[b][a])
        inverted.append(add)

    new = []
    for row in m_a:
        new_row = []
        for col in inverted:
            c = 0
            for d in range(len(inverted[0])):
                c += row[d] * col[d]
            new_row.append(c)
        new.append(new_row)

    return new
