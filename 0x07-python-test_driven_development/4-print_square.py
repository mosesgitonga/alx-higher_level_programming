#!/usr/bin/python3

def print_square(size):
    """
    Prints a square of 'x' characters with the specified size.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If `size` is not an integer.
        ValueError: If `size` is a negative value.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for index in range(size):
        print("#" * size)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
