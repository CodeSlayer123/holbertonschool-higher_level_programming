#!/usr/bin/python3
"""Checks if object is an instance of specified class"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is an instance of specified class, else Flase"""

    if type(obj) is a_class or isinstance(obj, a_class):
        return(True)
    else:
        return(False)
