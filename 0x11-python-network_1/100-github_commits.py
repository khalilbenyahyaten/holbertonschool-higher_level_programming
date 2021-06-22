#!/usr/bin/python3
"""github commits"""
import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    owner = argv[2]
    url = "https://api.github.com/repos/" + owner + "/" + repo + "/commits"
    reqs = requests.get(url)
    requets = reqs.json()[:10]
    for req in requets:
        sha = req['sha']
        commits = req['commit']['author']['name']
        print("{}: {}".format(sha, commits))
