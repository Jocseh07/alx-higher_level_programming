#!/bin/bash
# Takes in URL and display the methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
