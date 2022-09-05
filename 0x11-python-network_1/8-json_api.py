#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":

    if len(argv) == 1:
        q = ''
    else:
        q = argv[1]

    try:
        url = "http://0.0.0.0:5000/search_user"
        value = {'q': q}

        resp = requests.post(url, value).json()

        if len(resp) == 0:
            print("No result")
        else:
            print("[{}] {}".format(resp.get("id"), resp.get("name")))
    except ValueError:
        print("Not a valid JSON")
