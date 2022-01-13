#!/usr/bin/python3
"""Prints a square with the character #"""


def print_square(size):
    """Prints a square with the character # based from size variable"""

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        if type(size) == float:
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
