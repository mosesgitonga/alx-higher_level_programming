#!/usr/bin/python3
"""Module defining the BaseGeometry class"""


class BaseGeometry:
    """A base class for geometry-related operations"""

    def __init__(self):
        """Initializes a BaseGeometry instance"""
        pass

    def area(self):
        """Raises an exception indicating\
                that the area() method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is an integer and greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to validate.

        Raises:
            ValueError: If the value is less than or equal to 0.
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
