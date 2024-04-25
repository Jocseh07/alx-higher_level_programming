#!/bin/bash
# Takes in URL and display the methods
curl -s -w '%{http_code}' "$1" | cut -c 11-
