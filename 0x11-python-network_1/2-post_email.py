#!/usr/bin/python3
"""Takes in a URL an email, sends a POST request to the URL with the
email as parameter and displays the body of the response
(decoded in utf-8)."""


if __name__ == "__main__":
    from sys import argv
    from urllib import parse
    from urllib import request

    url = argv[1]
    email = argv[2]
    values = {'email': email, }
    data = parse.urlencode(values).encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
