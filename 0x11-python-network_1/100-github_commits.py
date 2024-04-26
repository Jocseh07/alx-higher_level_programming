#!/usr/bin/python3
"""Takes in GitHub credentials and uses API to display id."""


if __name__ == "__main__":
    import sys

    import requests
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1]
    )
    r = requests.get(url)
    commits = r.json()
    for a in range(10):
        print("{}: {}".format(
            commits[a].get("sha"),
            commits[a].get("commit").get("author").get("name")
        ))
