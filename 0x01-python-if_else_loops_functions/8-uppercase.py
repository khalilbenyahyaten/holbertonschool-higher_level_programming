#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 123:
            print("{:s}".format(chr(ord(str[i]) - 32)), end="")
        else:
            print("{:s}".format(str[i]), end="")
print("\n")
