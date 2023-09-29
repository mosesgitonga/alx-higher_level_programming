#!/usr/bin/python3
"""
taking github credentials to display my id
using github API
"""

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    auth = HTTPBasicAuth(argv[1], argv[2])
    url = "https://api.github.com/user"
    response = requests.get(url, auth=auth)
    print(response.json().get('id'))
