#!/usr/bin/python3
"""Checks if object is a subclass of specified class"""

def inherits_from(obj, a_class):
    """Returns True if object is subclass of specified class, else Flase"""

    if type(obj) is not a_class and isinstance(obj, a_class):
        return(True)
    else:
        return(False)