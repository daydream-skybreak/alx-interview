#!/usr/bin/python3
"""Rotate 2d Matrix"""


def rotate_2d_matrix(matrix):
    """rotates <matrix> 90deg clockwise"""
    transpose(matrix)
    for li in matrix:
        i, j = 0, len(li) - 1
        while i < j:
            li[i], li[j] = li[j], li[i]
            i += 1
            j -= 1


def transpose(matrix):
    """returns the transpose of <matrix>"""
    i = 0
    while i < len(matrix):
        j = i + 1
        while j < len(matrix[i]):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1
        i += 1
