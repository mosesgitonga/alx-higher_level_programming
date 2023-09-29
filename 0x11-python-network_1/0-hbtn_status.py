#!/usr/bin/python3
"""
script that fetches the content of a url
"""

import urllib.request
if __name__ == "__main__":
    try:
        with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
            body = response.read()
            decoded_content = body.decode('utf-8', 'replace')
            print("Body response:")
            print("\t- type: {}".format(type(body)))
            print("\t- content: {}".format(body))
            print("\t- utf-8 content: {}".format(decoded_content))
    except:
        pass