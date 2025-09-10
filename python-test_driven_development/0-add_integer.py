#!/usr/bin/python3
"""Module that defines add_integer function."""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as integers.

    Args:
        a: first number (int or float)
        b: second number (int or float, default = 98)

    Raises:
        TypeError: if a or b are not int or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
