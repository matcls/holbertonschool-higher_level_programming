#!/usr/bin/python3
"""Takes in a URL an email, sends a POST request to the URL with the
email as parameter and displays the body of the response
(decoded in utf-8)."""


if __name__ == "__main__":
    from sys import argv
    from urllib import error
    from urllib import request

    try:
        url = argv[1]
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code:", err.code)
