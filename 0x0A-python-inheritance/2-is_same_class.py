#!/usr/bin/python3
"""Checks if object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """Returns True if object is an instance of specified class, else Flase"""

    if type(obj) is a_class:
        return(True)
    else:
        return(False)
