#!/usr/bin/python3
"""Defines a function text_indentation"""


def text_indentation(text):
    """Method for prints a text with 2 new lines after '.?:' chars

    Args:
        text: The string to be printed

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print(text, end="")
