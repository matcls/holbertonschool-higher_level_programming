#!/bin/bash
# Make request to find the message "You got me!" from the server
curl -sLX PUT -H "Origin:HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
