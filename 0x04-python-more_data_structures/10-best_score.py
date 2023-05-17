#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) ==0:
        return None
    max = a_dictionary[next(iter(a_dictionary))]
    for key in a_dictionary:
        if max < a_dictionary[key]:
            max = a_dictionary[key]
    return max
