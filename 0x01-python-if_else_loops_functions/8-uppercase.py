#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if char >= chr(97) and char <= chr(122):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print("")
