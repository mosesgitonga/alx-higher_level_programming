#!/usr/bin/python3
"""
getting id from the url header
"""

import urllib.request
from sys import argv
if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(f"{url}") as response:
        print(response.headers['X-Request-Id'])
