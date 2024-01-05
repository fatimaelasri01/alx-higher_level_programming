#!/usr/bin/python3
"""Defines a locked class. """


class LockedClass:
    """Defines a class that restricts dynamically creating new instance
    attributes, allowing only 'first_name' as a valid attribute."""

    __slots__ = ["first_name"]
