#!/bin/bash
# Send a GET request to URL with header variable
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
