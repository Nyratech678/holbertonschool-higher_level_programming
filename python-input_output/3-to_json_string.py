#!/usr/bin/python3
import json
"""module that returns the JSON representation(object)"""


def to_json_string(my_obj):
    """function that returns the json representation of an object"""
    return json.dumps(my_obj)
