#!/usr/bin/python3
"""Fetches from a link using urllib package and display the X-Request-Id."""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as res:
        print(res.headers.get("X-Request-Id"))
