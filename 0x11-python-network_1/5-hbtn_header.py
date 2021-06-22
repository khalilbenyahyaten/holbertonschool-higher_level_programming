#!/usr/bin/python3
"""
hbtn header
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = requests.get(url)
    print(request.headers.get('X-Request-Id'))
