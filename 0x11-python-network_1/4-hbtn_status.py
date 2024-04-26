#!/usr/bin/python3
"""Fetches from a link using urllib package."""


if __name__ == "__main__":
    import requests

    body = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
