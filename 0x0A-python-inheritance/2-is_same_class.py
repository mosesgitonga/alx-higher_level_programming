#!/usr/bin/python3
"""function  for checking if class is same """


def is_same_class(obj, a_class):
    """
    arg:
        obj: type to compare
        a_class: class to compare
    Return:type
    """

    return type(obj) is a_class
