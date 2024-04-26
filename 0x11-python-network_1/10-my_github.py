#!/usr/bin/python3
"""Takes in GitHub credentials and uses API to display id."""


if __name__ == "__main__":
    import sys

    import requests
    from requests.auth import HTTPBasicAuth

    basic = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=basic)
    print(r.json().get("id"))
