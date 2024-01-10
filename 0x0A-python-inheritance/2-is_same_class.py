#!/usr/bin/python3
"""Module containing is_same_class method"""


def is_same_class(obj, a_class):
    """checks if the object is exactly an instance
    of a given class"""
    return type(obj) == a_class
