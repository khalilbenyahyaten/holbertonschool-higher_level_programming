#!/usr/bin/python3
"""hbtn status"""
import requests

if __name__ == "__main__":
    request = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(request.text.__class__))
    print("\t- content: {}".format(request.text))
