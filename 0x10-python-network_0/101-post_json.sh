#!/bin/bash
# Send a post request to URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
