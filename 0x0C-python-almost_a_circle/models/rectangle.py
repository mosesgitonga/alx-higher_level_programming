#!/usr/bin/python3
"""tests"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class that inherits from the Base class.
    Represents a rectangle with width, height, position (x, y), and an ID.
    """

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the position of the rectangle.
            y (int): The y-coordinate of the position of the rectangle.
            id (int): The ID of the rectangle.

        Returns:
            None
        """
        if id is not None:
            self.id = id
        else:
            self.id = self.__class__.__nb_objects + 1
            self.__class__.__nb_objects += 1
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new value for the width.

        Returns:
            None
        """
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new value for the height.

        Returns:
            None
        """
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.

        Returns:
            int: The x-coordinate of the position of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Args:
            value (int): The new value for the x-coordinate.

        Returns:
            None
        """
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.

        Returns:
            int: The y-coordinate of the position of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Args:
            value (int): The new value for the y-coordinate.

        Returns:
            None
        """
        self.__y = value
