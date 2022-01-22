#!/usr/bin/python3
"""Task 1 write file"""


def write_file(filename="", text=""):
    """Task 1 write file"""

    with open(filename, "w") as file:
        file.write(text)
    return(len(text))
