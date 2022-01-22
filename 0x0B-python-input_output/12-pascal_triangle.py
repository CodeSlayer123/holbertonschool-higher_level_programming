#!/usr/bin/python3
"""Task 12 triangle"""


def pascal_triangle(n):
    """Task 12 triangle"""
    if n <= 0:
        return ([])

    tri = [[]]
    for i in range(1, n + 1):
        m = 1
        for j in range(1, i + 1):
            tri.append(m)
            m = int(m * (i - j) / j)

    return(tri)
