#!/usr/bin/python3
"""importing json"""


def class_to_json(obj):
    """class to json
    Args:
        obj: object in class
    Return: dictionary
    """
    return obj.__dict__
