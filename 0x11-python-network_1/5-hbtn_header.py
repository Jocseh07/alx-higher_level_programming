#!/usr/bin/python3
"""Fetches from a link using urllib package and display the X-Request-Id."""


if __name__ == "__main__":
    import sys

    import requests

    body = requests.get(sys.argv[1])
    print(body.headers.get("X-Request-Id"))
