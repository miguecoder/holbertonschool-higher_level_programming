#!/usr/bin/python3
"""Function that append a string to text file"""


def append_write(filename="", text=""):
    """Function for append a string at thhe end of
    a txet file and return the number of characters added"""

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
