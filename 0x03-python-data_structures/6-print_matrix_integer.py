#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in matrix:
            for i, nbr in enumerate(row):
                print("{:d}".format(nbr), end="")
                if i < len(row) - 1:
                    print(" ", end="")
            print()
