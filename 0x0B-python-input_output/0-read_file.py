#!/usr/bin/python3

"""Task 0 read file"""


def read_file(filename=""):
    """Task 0 read file"""

    with open(filename, 'r') as txt_file:
        print(txt_file.read(), end="")
