#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        for index, value in enumerate(raw):
            if index != 0:
                print("{}".format(" "), end =  " ")
            print("{}".format(value), end = " ")
        print()
