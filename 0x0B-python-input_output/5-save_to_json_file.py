#!/usr/bin/python3
"""saving in json format"""
import json


def save_to_json_file(my_obj, filename):
    """aving in json format
    Args:
        my_obj: python object
        filename: the filename
    Return: e
    """
    with open(filename, mode="w+", encoding="utf-8") as myfile:
        json_rep = json.dumps(my_obj)
        myfile.write(json_rep)
