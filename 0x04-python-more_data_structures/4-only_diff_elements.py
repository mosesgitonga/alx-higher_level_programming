#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    newlist = set()
    for elem in set_1:
        if elem not in set_2:
            newlist.add(elem)
    for elem in set_2:
        if elem not in set_1:
            newlist.add(elem)
    return newlist
