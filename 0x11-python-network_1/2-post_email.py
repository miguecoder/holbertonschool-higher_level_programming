#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


from sys import argv
from urllib import request, parse

if __name__ == "__main__":

    url = argv[1]
    mail = argv[2]

    data = parse.urlencode({"email": mail}).encode('ascii')

    with request.urlopen(url, data) as res:
        html = res.read()
        print(html.decode('utf-8'))
