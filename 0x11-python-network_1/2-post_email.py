#!/usr/bin/python3
"""takes in a URL, sends a post request with email as param
and displays a docded utf-8 as response
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
