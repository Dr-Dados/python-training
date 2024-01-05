#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for el in range(len(matrix)):
        element = []
        for el1 in matrix[el]:
            el2 = el1*el1
            element.append(el2)
        new_matrix.append(element)
    return new_matrix
