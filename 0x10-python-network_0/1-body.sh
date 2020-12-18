#!/bin/bash
# Sends a GET request to the URL, and displays the body of the response
# Display only body of a 200 status code response
# Use curl
curl -sL "$1" # -L to follow locations (redirection)