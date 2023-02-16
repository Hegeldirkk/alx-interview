#!/usr/bin/python3
"""
interview ALX: Rotate 2D Matrix
SE: Diabakate Ikary
"""


def rotate_2d_matrix(matrix):
    """ 2D matrix
    rotate it 90 degrees clockwise.
    """
    n = len(matrix[0])
    [matrix[j].append(matrix[i].pop(0))
     for j in range(0, n) for i in range(n - 1, -1, -1)]
