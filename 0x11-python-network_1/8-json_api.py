#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = "http://0.0.0.0:5000/search_user"
    values = {"q": argv[1][0] if len(argv) > 1 else ""}
    response = requests.post(url, data=values)
    try:
        output = response.json()
        if output:
            print("[{}] {}".format(output.get("id"), output.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
