#!/usr/bin/env python3
"""
script that fetches the content of a url
"""

import urllib.request
with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body = response.read()
    decoded_content = body.decode('utf-8')
    print(
        f"Body response:\n\t- type: {type(body)}\n\t- content: \
        {body}\n\t- utf8 content: {decoded_content}")
