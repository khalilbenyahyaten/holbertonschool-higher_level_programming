#!/usr/bin/python3
"""
json api
"""
import sys
import requests

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, {'q': q})
    try:
        dire = r.json()
        id = dire.get('id')
        name = dire.get('name')
        if len(dire) == 0 or id is None or name is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
