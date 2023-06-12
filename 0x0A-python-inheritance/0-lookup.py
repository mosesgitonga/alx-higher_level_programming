#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object for which to retrieve the attributes and methods.

    Returns:
        A list of strings representing the names of available attributes and methods.

    """
    return dir(obj)
