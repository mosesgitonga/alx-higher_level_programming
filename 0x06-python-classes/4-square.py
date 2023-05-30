#!/usr/bin/python3
"""class Square"""


class Square:
    """Initialization """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        res = self.__size * self.__size
        return res
