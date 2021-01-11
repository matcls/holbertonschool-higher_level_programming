#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    values = {'email': email, }
    response = requests.post(url, data=values)
    print(response.text)
