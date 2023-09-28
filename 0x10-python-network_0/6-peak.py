#!/usr/bin/python3
"""
find peak
"""


def find_peak(list_of_integers):
    """
    finding the peak of a list
        -> it must return a single number
    """
    max_i = None
    for ele in list_of_integers:
        if max_i is None or max_i < ele:
            max_i = ele
    return max_i
