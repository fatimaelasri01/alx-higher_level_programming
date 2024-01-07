#!/usr/bin/python3
"""Defines a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Method for printing full name

    Args:
        first_name: person's first name
        last_name: person's last name

    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
