#!/usr/bin/python3
"""This is a Locked Class that prevents
the user from dynamically creating new instance attributes"""


class LockedClass(object):
    """
    Class that prevents the user from
    dynamically creating new instance attributes
    """
    __slots__ = 'first_name'

    def __init__(self, first_name=""):
        """Instantiation with optional first_name"""
        self.first_name = first_name
