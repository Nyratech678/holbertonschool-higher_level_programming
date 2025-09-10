#!/usr/bin/python3
"""Module that defines a function to print a person's full name."""

def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    This function validates that first_name and last_name are strings,
    and prints the formatted full name. If last_name is empty, it only
    prints the first name.

    Args:
        first_name (str): The first name of the person.
        last_name (str, optional): The last name of the person. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = first_name if not last_name else "{} {}".format(first_name, last_name)
    print("My name is {}".format(full_name))
