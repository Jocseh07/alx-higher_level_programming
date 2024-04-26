#!/usr/bin/python3
"""Takes in URL and email and send a POST request."""


if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as res:
        print(res.read().decode("utf-8"))
