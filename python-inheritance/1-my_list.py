#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """a method for printing the list in sorted order."""
    def print_sorted(self):
        """Prints the list in sorted order."""
        print(sorted(self))
