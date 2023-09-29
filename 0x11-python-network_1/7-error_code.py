#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
    to the URL and displays the body of the response
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = requests.get(argv[1])
    if response.status_code > 400:
        print(f"Error code: {response.status_code}")
