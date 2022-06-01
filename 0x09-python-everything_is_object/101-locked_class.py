#!/usr/bin/python3
"""This is a Locked Class hat prevents
the user from dynamically creating new instance attributes"""


class LockedClass(object):
    __slots__ = 'first_name'
