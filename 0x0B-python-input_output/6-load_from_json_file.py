#!/usr/bin/python3
"""loading from json"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The Python object created from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as myfile:
        json_data = myfile.read()
        pydata = json.loads(json_data)
        return pydata
