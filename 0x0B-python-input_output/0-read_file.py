#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text_file to stdout."""
    with open(filename, encoding="utf-8") as fl:
        print(fl.read(), end="")
