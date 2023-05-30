#!/usr/bin/python3
"""class Square"""


class Square:
    """Representing class Square"""

    __size = None

    def __init__(self, size=0):
        """Initializing
        Args:
             size(int): size of a square
        """

        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """calculates area of square"""
        res = self.__size * self.__size
        return res
