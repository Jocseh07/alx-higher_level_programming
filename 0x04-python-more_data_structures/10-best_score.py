#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        new = dict(sorted(a_dictionary.items(), key=lambda x: x[1]))
        new = sorted(new, reverse=True)
        return list(new.keys())[0]
    return "None"
