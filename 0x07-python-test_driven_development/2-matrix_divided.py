#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Module will divide all elements of matrix"""
    total = 0
    biggie_list = []
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    if not isinstance(matrix[0], list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    for i in range(len(matrix)):
        row_count = len(matrix[0])
        lil_list = []
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], float)
            and not isinstance(matrix[i][j], int):
                raise TypeError(
                    'matrix must be a matrix' +
                    ' (list of lists) of integers/floats'
                )
            total = matrix[i][j] / div
            total = round(total, 2)
            lil_list.append(total)
        if row_count != len(matrix[i]):
            raise TypeError(
                'Each row of the matrix must have the same size'
            )
        biggie_list.append(lil_list)
    return biggie_list
