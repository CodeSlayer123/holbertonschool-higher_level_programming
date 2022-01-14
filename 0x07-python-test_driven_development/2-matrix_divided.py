#!/usr/bin/python3
"""Divides numbers of a matrix"""


def matrix_divided(matrix, div):
    """Divides numbers of a matrix rounded to 2 decimal places"""
    # first batch of edgecases
    if type(matrix) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:  # check if variable matrix is a matrix
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])

    if size == 0:  # check for empty matrix
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:  # edgecases in matrix before copying
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
        for i in range(len(row)):
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    new_matrix = [x[:] for x in matrix]  # copy matrix

    for row in new_matrix:  # editing my own matrix
        for i in range(len(row)):
            row[i] = round(row[i] / div, 2)
    return(new_matrix)
