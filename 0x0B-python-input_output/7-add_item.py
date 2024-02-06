#!/usr/bin/python3
"""Adds all arguments to a python list and save to a file."""
import sys

if __name__ == "__main__":
    file1 = "5-save_to_json_file"
    file2 = "6-load_from_json_file"
    save_to_json_file = __import__(file1).save_to_json_file
    load_from_json_file = __import__(file2).load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
