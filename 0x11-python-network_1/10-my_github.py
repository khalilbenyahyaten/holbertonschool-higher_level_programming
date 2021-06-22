#!/usr/bin/python3
"""
my github
"""
from sys import argv
import requests


if __name__ == "__main__":
    username = argv[1]
    passwd = argv[2]
    req = requests.get('https://api.github.com/user', auth=(username, passwd))
    try:
        print(req.json()['id'])
    except Exception:
        print('None')
