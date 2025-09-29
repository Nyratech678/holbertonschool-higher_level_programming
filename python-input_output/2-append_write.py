#!/usr/bin/python3
"""module that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    Args:
    filename (str): name of the file
    text(str): string to append"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
