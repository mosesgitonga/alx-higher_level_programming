#!/usr/bin/python3
"""class base """
import json


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

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        x = "[]"
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return x
        else:
            jsonDict = json.dumps(list_dictionaries)
            return jsonDict

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_list = []
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]

        with open(filename, mode="w") as myfile:
            myfile.write(cls.to_json_string(json_list))

    def from_json_string(json_string):
        x = "[]"
        if json_string is None:
            return x
        else:
            real_data = json.loads(json_string)
            return real_data

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1, 1)

        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        attrs = ["id", "width", "height", "x", "y"]
        return {attr: getattr(self, attr) for attr in attrs}

    @classmethod
    def load_from_file(cls):
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
