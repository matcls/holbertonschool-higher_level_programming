#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
curl -sL "$1" # -L to follow locations (redirection)
