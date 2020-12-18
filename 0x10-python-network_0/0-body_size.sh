#!/bin/bash
# Sends a request to a given URL, 
# and displays the size of the body of the response
# The size must be displayed in bytes
# use curl

curl -s "$1" | wc -c
