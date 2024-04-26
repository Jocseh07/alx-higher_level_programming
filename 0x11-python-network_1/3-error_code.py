#!/usr/bin/python3
"""Takes in URL and email and send a POST request."""


if __name__ == "__main__":
    import sys
    from urllib import error, request

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code:", err.code)
