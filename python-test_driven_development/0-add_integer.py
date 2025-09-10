#!/usr/bin/python3
"""This module defines a function that adds two integers."""


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

    # NaN check: NaN != NaN
    if a != a or a == float("inf") or a == -float("inf"):
        raise TypeError("a must be an integer")
    if b != b or b == float("inf") or b == -float("inf"):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
