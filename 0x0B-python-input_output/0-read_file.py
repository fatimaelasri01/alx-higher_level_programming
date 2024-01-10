#!/usr/bin/python3
"""Module containing a function for reading a text file (UTF8)"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdouts"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
