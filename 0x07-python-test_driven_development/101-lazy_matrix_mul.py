#!/usr/bin/python3

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Computes the matrix multiplication of two matrices.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        The result of the matrix multiplication.
    """
    res = np.matmul(m_a, m_b)
    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/101-lazy_matrix_mul.txt")
