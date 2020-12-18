#!/bin/bash
# Send a request and displays only the status code of the response.
curl -so /dev/null -w "%{http_code}" "$1"
