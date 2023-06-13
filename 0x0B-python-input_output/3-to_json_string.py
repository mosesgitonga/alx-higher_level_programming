#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Convert a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        A JSON-formatted string representation of the object.
    """
    """
    This function converts a Python object to a JSON-formatted string.

    Parameters
    ----------
    my_obj : object
        The Python object to be converted.

    Returns
    -------
    str
        A JSON-formatted string representation of the object.
    """
    return json.dumps(my_obj)
