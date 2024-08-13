#!/usr/bin/python3
""" Given an n x n 2D matrix, rotate it 90 degrees clockwise
Prototype: def rotate_2d_matrix(matrix):
Return nothing. The matrix must be edited in-place.
The matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """ Function to rotate matrix 90 degrees clockwise"""
    for i, j in enumerate(zip(*reversed(matrix))):
        matrix[i] = list(j)


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_2d_matrix(matrix)
    print(matrix)
