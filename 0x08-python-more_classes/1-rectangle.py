#!/usr/bin/python3
"""class  rectangle"""


class Rectangle:
    """representing a rectagle"""

    def __init__(self, width=0, height=0):
        """initializing the rectangle
        Args:
            width: the width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """width function
        Args:
            value(int): value of the width
        Raises:
            TypeError: when type is not int
            ValueError:when value is less than 0

        Return: value of rectangle
        """
        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """this height setter"""
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        self.__height = value
