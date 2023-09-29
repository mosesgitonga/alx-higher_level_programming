#!/usr/bin/python3
"""post request that takes an email address in argumnet
"""


if __name__ == "__main__":
    from sys import argv
    import requests
    payload = {"Your email is: ": argv[2]}
    response = requests.post(argv[1], data=payload)
    print(response)