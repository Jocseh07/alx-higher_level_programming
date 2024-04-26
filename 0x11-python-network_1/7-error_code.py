#!/usr/bin/python3
"""Takes in URL and email and send a request and display the body."""


if __name__ == "__main__":
    import sys

    import requests

    url = sys.argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
