#!/usr/bin/python3
"""takes in a URL, sends a request with
and displays a docded utf-8 as response
"""
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('Error code: ', e.code)
    else:
        print(response.read().decode("utf-8"))
