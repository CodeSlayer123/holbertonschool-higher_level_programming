#!/usr/bin/python3
"""Task 2 append write"""


def append_write(filename="", text=""):
    """Task 2 append write"""

    with open(filename, "a") as file:
        file.write(text)
    return(len(text))
