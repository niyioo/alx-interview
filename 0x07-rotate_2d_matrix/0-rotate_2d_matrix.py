#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def transpose(matrix):
    """
    Transpose the given matrix in-place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_rows(matrix):
    """
    Reverse each row of the given matrix in-place.
    """
    n = len(matrix)
    for i in range(n):
        matrix[i] = matrix[i][::-1]


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix 90 degrees clockwise.
    """
    # Transpose the matrix
    transpose(matrix)

    # Reverse each row
    reverse_rows(matrix)
