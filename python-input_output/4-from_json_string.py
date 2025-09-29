#!/usr/bin/python3
"""Module that return an object in json string format"""
import json


def from_json_string(my_str):
    """Function that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (str): JSON string to be converted to object

    Returns:
        Object (Python data structure) represented by a JSON string
    """
    return json.loads(my_str)
