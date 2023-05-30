#!/usr/bin/python3
"""Class square"""


class Square:
    """Representing class square"""

    __size = None

    def __init__(self, size=0):
        """Initializing

        Args:
            size (int): Size of a square
        """

        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
