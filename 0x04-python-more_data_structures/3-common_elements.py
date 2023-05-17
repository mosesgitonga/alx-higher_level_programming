#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = []
    for a, b in zip(set_1, set_2):
        if a == b:
            common.append(a)
    return common
