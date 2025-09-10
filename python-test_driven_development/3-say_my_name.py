#!/usr/bin/python3
"""This module contains a function that prints a full name."""

def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

    Args:
        first_name (str): The first name to print.
        last_name (str, optional): The last name to print. Defaults to "".

    Raises:
        TypeError: If first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
