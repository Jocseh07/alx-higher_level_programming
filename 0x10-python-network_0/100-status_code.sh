#!/bin/bash
# Takes in URL and display the methods
curl -s -o /dev/null -w "%{http_code}" "$1"
