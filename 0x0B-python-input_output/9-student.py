#!/usr/bin/python3

"""
This class represents a student.

Attributes:
    first_name (str): The student's first name.
    last_name (str): The student's last name.
    age (int): The student's age.

Methods:
    to_json(self): Returns a dictionary representation of the student.
"""


class Student:

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary representation of the student.

        Returns:
            dict: A dictionary representation of the student.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
