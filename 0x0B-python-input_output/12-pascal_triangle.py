#!/usr/bin/python3
"""Task 12 triangle"""


def pascal_triangle(n):
    """Task 12 triangle"""

    mother_matrix = []
    if n <= 0:
        return (mother_matrix)

    toddler = [1]
    for i in range(n):
        mother_matrix.append(toddler)
        big_sis = []
        big_sis.append(toddler[0])
        for i in range(len(toddler) - 1):
            big_sis.append(toddler[i] + toddler[i + 1])
        big_sis.append(toddler[-1])
        toddler = big_sis
    return(mother_matrix)
