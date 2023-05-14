#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for index, value in enumerate(raw):
            print("{}".format(value), end = " ")
        print("")
