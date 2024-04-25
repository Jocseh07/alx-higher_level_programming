#!/bin/bash
# Send a request to URL and display the size
curl -s "$1" | wc -c
