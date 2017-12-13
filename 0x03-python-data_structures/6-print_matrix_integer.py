#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        for row in a:
            print('{:d}'.format(row), end="\n")
