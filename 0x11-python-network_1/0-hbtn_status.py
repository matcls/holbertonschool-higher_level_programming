#!/usr/bin/python3
"""Fetches a URL"""


if __name__ == "__main__":
    from urllib import request

    url = 'https://intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type:', type(html))
        print('\t- content:', html)
        print('\t- utf8 content:', html.decode('utf-8'))
