#!/usr/bin/python3
"""Island perimeter solver"""


def island_perimeter(grid):
    """solves Island perimeter"""
    (row, column) = (len(grid), len(grid[0]))
    perimeter = 0
    for i in range(row):
        for j in range(column):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == row - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == column - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
    return perimeter
