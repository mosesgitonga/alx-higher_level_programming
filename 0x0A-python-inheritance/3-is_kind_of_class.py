#!/usr/bin/python3
"""check if is class"""


def is_kind_of_class(obj, a_class):
    """if is instance

    arg:
        obj: object
        a_class: class intace
    Return: True pr False
    """
    return isinstance(obj, a_class)
