#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for index in range(len(raw)):
            if index != len(raw) - 1:
                print("{:d} ".format(raw[index]),end = "")
            else:
                print("{:d}".format(raw[index]),end = "")
        print()
