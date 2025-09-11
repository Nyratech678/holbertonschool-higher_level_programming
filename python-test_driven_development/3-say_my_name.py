#!/usr/bin/python3
"""Module that defines a function to print a person's full name."""

def say_my_name(first_name, last_name=""):
    """Prints 'My name is <first_name> <last_name>'.

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

    # Handle edge cases for empty or whitespace-only strings
    first_stripped = first_name.strip()
    last_stripped = last_name.strip()

    if not first_stripped and not last_stripped:
        print("My name is")
    elif last_stripped:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
