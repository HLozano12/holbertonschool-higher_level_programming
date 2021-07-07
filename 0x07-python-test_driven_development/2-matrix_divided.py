#!/usr/bin/python3
""" function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """ Divides matrix by div """

    """ Tests the  matrix and elements in matrix """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    """ Tests its a numbr or div of 0 """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda num:
                          list(map(lambda num:
                                   round(num / div, 2), num)), matrix))
    return new_matrix