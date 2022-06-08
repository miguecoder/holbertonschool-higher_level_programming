#!/usr/bin/python3
"""Class MyList"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        return print(sorted(self))
