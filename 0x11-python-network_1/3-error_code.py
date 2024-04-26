#!/usr/bin/python3
"""Takes in URL and email and send a POST request."""


if __name__ == "__main__":
    import sys
    import urllib.error
    import urllib.request

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            print(res.read().decode("UTF-8"))
    except urllib.error.HTTPError as er:
        print("Error code: ".format(er.code))
