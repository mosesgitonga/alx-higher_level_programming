#!/usr/bin/python3
"""class base """
import json


class Base:
    """
    Represents a base class.

    Attributes:
        __nb_objects (int): A class variable to keep track of the number of instances created.
        id (int): An identifier for the instance.

    Methods:
        __init__(self, id=None): Initializes a new instance of the Base class.
        to_json_string(list_dictionaries): Converts a list of dictionaries to a JSON string.
        save_to_file(cls, list_objs): Saves a list of objects to a file in JSON format.
        from_json_string(json_string): Converts a JSON string to a list of dictionaries.
        create(cls, **dictionary): Creates a new instance based on a dictionary of attributes.
        update(self, *args, **kwargs): Updates the attributes of an instance.
        to_dictionary(self): Converts the instance attributes to a dictionary.
        load_from_file(cls): Loads a list of instances from a JSON file.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int, optional): An identifier for the instance.
                If provided, the instance's id is set to the provided value.
                If not provided, the instance's id is automatically assigned as the next available number.

        Returns:
            None
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """

        x = "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return x
        else:
            jsonDict = json.dumps(list_dictionaries)
            return jsonDict

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file in JSON format.

        Args:
            list_objs (list): A list of objects to be saved.

        Returns:
            None
        """

        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode="w") as myfile:
            myfile.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries converted from the JSON string.
        """

        x = "[]"
        if json_string is None:
            return x
        else:
            real_data = json.loads(json_string)
            return real_data

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance based on a dictionary of attributes.

        Args:
            dictionary (dict): A dictionary containing the attributes of the instance.

        Returns:
            object: A new instance of the class with the provided attributes.
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """
        Updates the attributes of an instance.

        Args:
            *args: Variable length argument list containing attribute values.
            **kwargs: Arbitrary keyword arguments representing attribute-value pairs.

        Returns:
            None
        """

        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the instance attributes to a dictionary.

        Returns:
            dict: A dictionary containing the instance attributes.
        """

        attrs = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a JSON file.

        Returns:
            list: A list of instances loaded from the JSON file.
        """

        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r") as myfile:
                json_str = myfile.read()
                if json_str:
                    dictionaries = cls.from_json_string(json_str)
                    instances = [cls.create(**dictionary) for dictionary in dictionaries]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []

