#!/usr/bin/python3
"""
post email
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    body = requests.post(url, value)
    print(body.text)
    