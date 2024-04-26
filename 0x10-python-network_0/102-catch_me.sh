#!/bin/bash
# Send a request to URL and display the body
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
