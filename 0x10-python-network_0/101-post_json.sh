#!/bin/bash
# Send a post request to URL
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
