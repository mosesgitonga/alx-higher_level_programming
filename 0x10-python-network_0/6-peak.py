#!/usr/bin/python3
"""
find peak
"""


def find_peak(list_of_integers):
    """
    finding the peak of a list
        -> it must return a single number
    """
    list = list_of_integers
    for i in range(len(list)):
        if list[i] + 1 > list[i] and list[i] > list[i] - 1:
            return list[i]
        else:
            pass
