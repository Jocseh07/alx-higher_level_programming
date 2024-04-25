#!/bin/bash
# Takes in URL and display the methods
curl -sI "$1" | cut -d " " -f 2 | head -1
