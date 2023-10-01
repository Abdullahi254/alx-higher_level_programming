#!/usr/bin/python3
"""takes in a letter and sends a POST request to 
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No result")
    else:
        try:
            url = "http://0.0.0.0:5000/search_user"
            q = sys.argv[1]
            r = requests.post(url, data={"q": q if q is not None else ""})
            if not r.json():
                print("No result")
            else:
                print("[{}] {}".format(r.json().get("id"), r.json().get("name")))
        except ValueError:
            print("Not a valid JSON")

