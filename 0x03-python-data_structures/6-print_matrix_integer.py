#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for first in range(len(matrix)):
        for second in range(len(matrix[first])):
            print('{}'.format(matrix[first][second]), end=" ")
        print("\n", end="")
