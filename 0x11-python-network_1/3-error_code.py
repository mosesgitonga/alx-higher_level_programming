#!/usr/bin/python3
"""pythin script that takes in url and returns
the content in the response"""


if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    from sys import argv
    try:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print(f"Error code: {e.status}")
