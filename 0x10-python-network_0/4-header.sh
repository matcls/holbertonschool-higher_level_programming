#!/bin/bash
# Send a GET request to a given URL with a header variable, show the body of the response.
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
