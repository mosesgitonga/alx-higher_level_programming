#!/usr/bin/python3
"""This module defines the Square class."""


class Square:
    """Represents a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square object.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position of the square (default is (0, 0)).
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Getter for size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size attribute.

        Args:
            value (int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position attribute.

        Args:
            value (tuple): The new position value.
        """
        if len(value) != 2 or not \
           all(isinstance(num, int) and num >= 0 for num in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The calculated area.
        """
        return self.__size * self.__size

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
