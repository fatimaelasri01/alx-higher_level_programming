#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
           sq_row = [nbr ** 2 for nbr in row]
           new_matrix.append(sq_row)

    return new_matrix
