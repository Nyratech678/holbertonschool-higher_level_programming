#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        If attrs is a list of strings, only attribute names contained in this
        list must be retrieved.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                                    Defaults to None.

        Returns:
            dict: Dictionary representation of the Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        for key, value in json.items():
            setattr(self, key, value)
