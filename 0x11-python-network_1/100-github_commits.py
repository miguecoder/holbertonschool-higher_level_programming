#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to
solve this challenge.
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    for commit in response.json()[:10]:
        print(
            "{}: {}".format(
                commit['sha'], commit['commit']['author']['name']
            )
        )
