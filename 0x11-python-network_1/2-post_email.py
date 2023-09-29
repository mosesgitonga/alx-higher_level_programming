#!/usr/bin/python3
"""
python script that takes in a url
"""


import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(f"{argv[1]}") as response:
        email = {
            "Your email is": argv[2]
        }
        encoded_email = urllib.parse.urlencode(email)
        encoded_email = encoded_email.encode('ascii')
        req = urllib.request.Request(argv[1], encoded_email)
        with urllib.request.urlopen(req) as response:
            res_content = response.read()
            print(res_content.decode('utf-8'), "replace")