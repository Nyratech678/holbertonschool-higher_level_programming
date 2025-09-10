#!/usr/bin/python3
"""
This module defines a function that adds two integers.
It ensures type checking and converts floats to integers before adding.
"""


def add_integer(a, b=98):
    """
    Add two integers and return the result as an integer.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.

    Returns:
        int: The sum of a and b, converted to an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
