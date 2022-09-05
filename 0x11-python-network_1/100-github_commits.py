#!/usr/bin/python3
"""
Python script that takes 2 arguments in order to
solve this challenge:
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line).
"""

from sys import argv
import requests

if __name__ == "__main__":
    repo = argv[1]
    username = argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(username, repo)
    response = requests.get(url)
    for commit in response.json()[:10]:
        print(
            "{}: {}".format(
                commit['sha'], commit['commit']['author']['name']
            )
        )
