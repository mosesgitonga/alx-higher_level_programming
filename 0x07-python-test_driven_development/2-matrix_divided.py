#!/usr/bin/python3
"""Function to divide matrix"""


def matrix_divided(matrix, div):
    """Divide matrix
    Args:
        matrix: List of lists
        div (int): Number to divide matrix by
    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats
        TypeError: If rows in the matrix have different sizes
        TypeError: If div is not an int
        ZeroDivisionError: If div is zero
    Returns:
        new_matrix: Matrix after division
    """

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
    if not all(isinstance(num, (int, float))for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_sizes = [len(row) for row in matrix]
    if not all(size == row_sizes[0] for size in row_sizes):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(column / div, 2) for column in row]
        new_matrix.append(new_row)

    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
