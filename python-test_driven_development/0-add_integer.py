#!/usr/bin/python3
"""This module defines a function that adds two integers."""


import math


def add_integer(a, b=98):
    """Add two integers or floats, and return the result as an integer.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Raises:
        TypeError: If a or b are not integers/floats, or if they are NaN/inf.

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if math.isnan(a) or math.isinf(a):
        raise TypeError("a must be an integer")
    if math.isnan(b) or math.isinf(b):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
