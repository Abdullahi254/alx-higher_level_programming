#!/usr/bin/python3
"""takes in a URL, sends a post request with email as param
and displays a docded utf-8 as response
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    r = requests.post(url, data=values)
    print(r.text)
