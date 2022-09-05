#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""


import requests as req

if __name__ == "__main__":
    body = req.get("https://intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: \
        {}".format(type(body.text), body.text))
