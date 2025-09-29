#!/usr/bin/python3
"""Module that write an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj (any): object to be written
        filename (str): name of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
