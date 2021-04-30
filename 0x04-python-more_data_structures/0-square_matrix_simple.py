#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda h:h ** 2, idx)) for idx in matrix])
