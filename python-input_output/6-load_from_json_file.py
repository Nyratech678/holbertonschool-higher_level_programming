#!/usr/bin/python3
"""Module that creates an Object from a Json file"""
import json


def load_from_json_file(filename):
    """Functions that creates an Object from a Json file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
