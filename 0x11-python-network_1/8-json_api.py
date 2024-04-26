#!/usr/bin/python3
"""Takes in letter and send a POST request with letter as parameter."""


if __name__ == "__main__":
    import sys

    import requests

    if len(sys.argv) == 1:
        letter = '""'
    else:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    value = {"q": letter}
    r = requests.post(url, data=value)
    try:
        res = r.json()
        if res == {}:
            print("No Result")
        else:
            print("[{}] {}".format(res.get("id"), res.get("name")))
    except ValueError:
        print("Not a valid JSON")
