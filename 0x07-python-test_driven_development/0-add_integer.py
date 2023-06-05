#!/usr/bin/python3
"""function to add integers"""


def add_integer(a, b=98):
    """Add integer
    Args:
        a (int): first int
        b (int, optional): second int
    Raises:
        TypeError: if a and be are not int or float

    Returns:
        int: sum of integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return a + b


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/0-add_integer.txt')
