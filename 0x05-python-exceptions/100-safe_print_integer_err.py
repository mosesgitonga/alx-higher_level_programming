#!/usr/bin/python3

def safe_print_integer_err(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            raise TypeError("{} is not an intger".format(value))
    except TypeError as te:
        return False
