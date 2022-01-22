#!/usr/bin/python3
"""Task 12 triangle"""


def pascal_triangle(n):
    """Task 12 triangle"""
    if n <= 0:
        return ([])

    mother_matrix = []
    toddler = [1]
    for i in range(n):
        mother_matrix.append(toddler)
        mother_matrix = []
        mother_matrix.append(toddler[0])
        for i in range(len(toddler)-1):
            mother_matrix.append(toddler[i] + toddler[i+1])
        mother_matrix.append(toddler[-1])
        list = mother_matrix
