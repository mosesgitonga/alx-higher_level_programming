#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if isinstance(value, int):
            print("{:d}".format(value))
            return True
        else:
            return False

    except TypeError:
        raise TypeError("{:s} is not an integer".format(value))
