#!/usr/bin/python3
""" a Python script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    if len(argv) <= 1:
        a = ""
    else:
        a = argv[1]
    payload = {'q': a}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data=payload)
    try:
        res = response.json()
        if res:
            print(f"[{res.get('id')}] {res.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")