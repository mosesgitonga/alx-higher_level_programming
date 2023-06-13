#!/usr/bin/python3


def read_file(filename=""):
    """function to read file
        Args:
            filename: the file to read

    """

    with open(filename, mode="r", encoding="utf-8") as my_file:
        print(my_file.read())
