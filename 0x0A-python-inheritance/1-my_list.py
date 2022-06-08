#!/usr/bin/python3
"""This module have the Class MyList"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Function that print the list sorted"""
        print(sorted(self))
