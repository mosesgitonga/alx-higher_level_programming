#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """if is instance

    arg:
        obj: object
        a_class: class intace
    Return: True pr False
    """

    return type(obj) is not a_class
