#!/usr/bin/python3
"""implements pascals triangle"""


def pascal_triangle(n):
    """ returns pascal triangle for a given integer 'n'
    @param: n
    returns an empty list for n <= 0
    """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        if len(pascal) == 0:
            pascal.append([1])
        elif len(pascal) == 1:
            pascal.append([1, 1])
        else:
            new = []
            new.append(pascal[-1][0])
            for i in range(len(pascal[-1]) - 1):
                new.append(pascal[-1][i] + pascal[-1][i + 1])
            new.append(pascal[-1][-1])
            pascal.append(new)
    return pascal
