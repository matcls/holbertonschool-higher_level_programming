#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response."""


if __name__ == "__main__":
    import requests
    from sys import argv
    try:
        url = argv[1]
        response = requests.get(url)
        print(response.text)
    except requests.exceptions.RequestException as err:
        print('Error code:', err.response.status_code)
