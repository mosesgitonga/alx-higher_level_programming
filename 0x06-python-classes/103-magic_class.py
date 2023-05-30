#!/usr/bin/python3
"""This module defines the MagicClass."""


import math


class MagicClass:
    """Represents a magical circle."""

    def __init__(self, radius):
        """Initialize a MagicClass object with a given radius.

        Args:
            radius (int or float): The radius of the circle.
        Raises:
            TypeError: If the radius is not a number.
        """
        self.set_radius(radius)

    def set_radius(self, radius):
        """Set the radius of the circle.
        Args:
            radius (int or float): The radius of the circle.
        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def get_radius(self):
        """Get the radius of the circle.

        Returns:
            int or float: The radius of the circle.
        """
        return self.__radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The calculated area.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The calculated circumference.
        """
        return 2 * math.pi * self.__radius
