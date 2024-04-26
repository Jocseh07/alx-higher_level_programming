#!/usr/bin/python3
"""Takes in URL and email and send a POST request."""


if __name__ == "__main__":
    import sys

    import requests

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
