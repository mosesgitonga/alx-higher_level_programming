#!/usr/bin/python3
"""empty class"""


class BaseGeometry:
    """intializing class"""
    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate value
        Args:
            name: name entered
            value: value to validate
            Raises:
                ValueError: must be greater than 0
                TypeError: must be an int
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
