#!/bin/bash
# Takes in URL and display the methods
curl -sI-w '%{http_code}' "$1"
