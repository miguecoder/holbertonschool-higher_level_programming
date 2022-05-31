#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    lol = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(div, (float, int)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not type(matrix) is list or len(matrix) == 0:
        raise TypeError(lol)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(lol)
        if not len(matrix[0]) == len(row):
            raise TypeError('Each row of the matrix must have the same size')
        for item in row:
            if not isinstance(item, (float, int)):
                raise TypeError(lol)
    return [[round(item / div, 2) for item in row] for row in matrix]
