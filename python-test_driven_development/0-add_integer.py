#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers or floats, and return the result as an integer.

    Args:
        a (int or float): First number.
        b (int or float, optional): Second number. Defaults to 98.

    Raises:
        TypeError: If a or b are not integers or floats.
        OverflowError: If a or b are too large (infinite or NaN).

    Returns:
        int: The sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Protection contre les floats spéciaux
    if a != a or b != b:  # NaN
        raise OverflowError("cannot convert NaN to integer")
    if a in (float("inf"), float("-inf")) or b in (float("inf"), float("-inf")):
        raise OverflowError("cannot convert float infinity to integer")

    return int(a) + int(b)
