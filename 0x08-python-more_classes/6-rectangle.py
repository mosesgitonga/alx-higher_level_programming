#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """
    Rectangle class represents a rectangle shape.

    Attributes:
        number_of_instances (int): Keeps track \
                of the number of instances created.

    Methods:
        __init__(self, width=0, height=0): Initializes \
                a new instance of the Rectangle class.
        width (int): Width of the rectangle.
        height (int): Height of the rectangle.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter \
                of the rectangle.
        __str__(self): Returns a string representation of the rectangle\
                using '#' characters.
        __repr__(self): Returns a string representation of the rectangle \
        that can be used to recreate an instance.
        __del__(self): Performs necessary actions when an instance \
        of Rectangle is deleted.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): Width of the rectangle. Defaults to 0.
            height (int): Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: Width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): Value to set as the width of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: Height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): Value to set as the height of the rectangle.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: Area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: Perimeter of the rectangle.
        """
        return 0 if self.__width == 0 or self.__height == 0 \
                else (self.__height + self.__width) * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle using '#' characters.

        Returns:
            str: String representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("#" * self.__width + "\n") * self.__height

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can \
                be used to recreate an instance.

        Returns:
            str: String representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Performs necessary actions when an instance of Rectangle is deleted.

        Returns:
            None
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
