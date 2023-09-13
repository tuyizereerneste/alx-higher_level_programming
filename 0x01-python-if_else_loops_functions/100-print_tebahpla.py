#!/usr/bin/python3

"""Print the alphabet altnating lowercase and upper case
not followed by a new line.
"""
for letter in range(122, 96, -1):
    if letter % 2 != 0:
        print("{}".format(chr(letter -32)), end="")
    else:
        print("{}".format(chr(letter)), end="")
