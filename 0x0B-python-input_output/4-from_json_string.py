#!/usr/bin/python3
"""json to python datastructure"""
import json


def from_json_string(my_str):
    """convert json format to python data
        Args:
            my_str: json string
        Return: pythonic data
    """
    data = json.loads(my_str)
    return data
