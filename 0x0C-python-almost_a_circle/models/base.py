#!/usr/bin/python3
"""class base """


class Base:
    """
    Represents a base class.

    Attributes:
        __nb_objects (int): A class variable to keep \
                track of the number of instances created.
        id (int): An identifier for the instance.

    Methods:
        __init__(self, id=None): Initializes a new instance of the Base class.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An identifier for the instance.\
                    If provided, the instance's id is set to\
                    the provided value.
                If not provided, the instance's id is automatically \
                        assigned as the next available number.

        Returns:
            None
        """
        self.id = id
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
