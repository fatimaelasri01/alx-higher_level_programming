#!/usr/bin/python3
"""Defines a function: print_square"""


def print_square(size):
    """Method for printing a square with # character

    Args:
        size: The int size of the square

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is less than 0

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")
