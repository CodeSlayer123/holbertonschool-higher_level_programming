#!/usr/bin/python3
"""Divides numbers of a matrix"""


def matrix_divided(matrix, div):
    """Divides numbers of a matrix rounded to 2 decimal places"""
    if type(matrix) != list:
            raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [x[:] for x in matrix]
    size = len(matrix[0])

    for row in new_matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix\
                            must have the same size")

        for i in range(len(row)):
            if type(i) != int and type(i) != float:
                raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")

            row[i] = round(row[i] / div, 2)
    return(new_matrix)
