#!/usr/bin/python3


"""
Writes a string to a text file (UTF8)
and returns the number of characters written.

Args:
    filename: The path of the file to write to.
    text: The string to write to the file.

Returns:
    The number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    and returns the number of characters written.

    Args:
        filename: The path of the file to write to.
        text: The string to write to the file.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
