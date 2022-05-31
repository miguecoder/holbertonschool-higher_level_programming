#!/usr/bin/python3
"""Function that print a text with 2 new lines after characters: ., ? and :"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after characters: ., ? and :
    """
    sig = True
    if not type(text) is str:
        raise TypeError("text must be a string")

    for item in text:
        if item == ' ' and sig is True:
            continue
        if item in ['.', '?', ':']:
            print(item, end='')
            print("\n")
            sig = True
        else:
            print(item, end='')
            sig = False
