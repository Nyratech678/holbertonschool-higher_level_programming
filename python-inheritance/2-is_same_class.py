#!/usr/bin/python3
"""Defines a function that check if an object is exactly."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class."""
    return type(obj) is a_class
