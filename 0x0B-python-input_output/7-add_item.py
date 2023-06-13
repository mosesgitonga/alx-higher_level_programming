#!/usr/bin/python3
"""adding items to a list"""
from json import dump, load
from os import path
from typing import List
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


def add_item_to_list(items: List[str], filename: str):
    """Add items to a list and save it to a JSON file.

    Args:
        items (List[str]): The items to add to the list.
        filename (str): The name of the JSON file to save the list.

    Returns:
        None
    """
    if path.exists(filename):
        existing_list = load_from_json_file(filename)
    else:
        existing_list = []

    existing_list.extend(items)

    save_to_json_file(existing_list, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    add_item_to_list(args, "add_item.json")
