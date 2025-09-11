#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    start_of_line = True

    while i < len(text):
        if start_of_line and text[i] == ' ':
            i += 1
            continue

        start_of_line = False
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            start_of_line = True
            i += 1
            # Skip spaces after punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
