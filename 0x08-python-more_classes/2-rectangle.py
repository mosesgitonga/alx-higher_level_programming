#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """initializing rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            ValueError("width must be >= 0")
        if not isinstance(value, int):
            TypeError("width must be an integer")

        self.__width = value

    @property
    def height(self):
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return (self.__height * 2) + (self.__width * 2)
