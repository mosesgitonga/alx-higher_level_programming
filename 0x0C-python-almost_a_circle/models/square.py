#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from the Rectangle class.
    Represents a square with a size, position (x, y), and an ID.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the position of the square.
            y (int): The y-coordinate of the position of the square.
            id (int): The ID of the square.

        Returns:
            None
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (int): The new value for the size.

        Returns:
            None
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the Square object.

        Returns:
            str: A string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Square instance.

        Args:
            *args: Variable length argument list containing attribute values.
            **kwargs: Arbitrary keyword arguments representing attribute-value pairs.

        Returns:
            None
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(args):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

