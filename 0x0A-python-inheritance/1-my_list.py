#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """creates a new class MyList that inherits from list"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
