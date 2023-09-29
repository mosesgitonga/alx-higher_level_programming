#!/usr/bin/python3
"""using requsts to fetch url"""


if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    res = response.content.decode('utf-8')
    print(f"Body response:\n\t- type: {type(res)}\n\t- content: {res}")
