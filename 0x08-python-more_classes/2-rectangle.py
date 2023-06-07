#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """initializing rectangle
    Args:
        width (int): width of rect
        height (int): height of rect

    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """width setler
        Args:
            value (int): value of width
        Raises:
            ValueError: error
            TypeError: error
        Return: value (int)
        """

        if value < 0:
            ValueError("width must be >= 0")
        if not isinstance(value, int):
            TypeError("width must be an integer")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        """height setler
        Args:
            value (int): value of height
        Raises:
            ValueError: error
            TypeError: error
        Return: value (int)
        """

        if not isinstance(value, int):
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)
