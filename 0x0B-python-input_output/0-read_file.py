#!/usr/bin/python3

"""
Reads a text file (UTF8) and returns the contents of the file as a string.

Args:
    filename: The path of the file to read.

Returns:
    The contents of the file as a string.
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and returns the contents of the file as a string.

    Args:
        filename: The path of the file to read.

    Returns:
        The contents of the file as a string.
    """

    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
