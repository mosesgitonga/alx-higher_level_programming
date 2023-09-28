#!/usr/bin/python3
"""
finding the peak of a list
    -> it must return a single number
"""
def find_peak(list_of_integers):
    list = list_of_integers
    for i in range(len(list)):
        if list[i] + 1 > list[i] and list[i] > list[i] - 1:
            return list[i]
        else:
            pass
            