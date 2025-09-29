#!/usr/bin/python3
"""module that returns the JSON representation(object)"""
import json


def to_json_string(my_obj):
    """function that returns the json representation of an object"""
    return json.dumps(my_obj)
