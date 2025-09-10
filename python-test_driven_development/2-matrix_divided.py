#!/usr/bin/python3
"""
This module defines a function matrix_divided(matrix, div)
that divides all elements of a matrix by div.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix (list of list of int/float): The matrix to be divided.
        div (int or float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows are not all the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        list of list of float: A new matrix with elements divided by div,
                               rounded to 2 decimal places.

    Example:
        >>> matrix = [[1, 2], [3, 4]]
        >>> matrix_divided(matrix, 2)
        [[0.5, 1.0], [1.5, 2.0]]
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) == 0 or any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
