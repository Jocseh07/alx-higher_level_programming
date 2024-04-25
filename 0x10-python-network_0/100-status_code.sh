#!/bin/bash
# Takes in URL and display the methods
curl -sw '%{http_code}' "$1" | cut -c 11-
