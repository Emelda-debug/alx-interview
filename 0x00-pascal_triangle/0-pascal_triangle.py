#!/usr/bin/python3
"""
function that returns a list of lists of integers representing
the Pascal’s triangle of n:
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    and n is assumed to always be an integer
    """
    x = []
    if n <= 0:
        return x
    x = [[1]]
    for i in range(1, n):
        current_row = [1]
        for j in range(len(x[i - 1]) - 1):
            prev_row = x[i - 1]
            current_row.append(x[i - 1][j] + x[i - 1][j + 1])
        current_row.append(1)
        x.append(current_row)
    return x
