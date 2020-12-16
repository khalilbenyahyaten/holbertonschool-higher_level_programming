#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        f = ""
    else:
        f = sentence[0]
    return len(sentence), f
