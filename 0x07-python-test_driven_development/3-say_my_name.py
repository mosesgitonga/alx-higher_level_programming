#!/usr/bin/python3


"""
This function prints a greeting with the user's name.

Args:
    first_name (str): The user's first name.
    last_name (str, optional): The user's last name. Defaults to an empty string.

Returns:
    None.
"""

def say_my_name(first_name: str, last_name: str = "") -> None:
    # Check if the first name is a string.
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # Check if the last name is a string.
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # If the last name is not empty, print the greeting with the user's full name.
    if last_name:
        print(f"My name is {first_name} {last_name}")

    # Otherwise, print the greeting with the user's first name only.
    else:
        print(f"My name is {first_name}")

