#!/usr/bin/python3


def multiple_returns(sentence):
    tuplea = ()
    if len(sentence) == 0:
        tuplea = ("None",)
    else:
        tuplea = len(sentence), sentence[0]
    return tuplea
