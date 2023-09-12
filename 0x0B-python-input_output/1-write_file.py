#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Arguments:
    filename (str): name of the file to write on.
    text (str): The text to write to the file.
    Returns:
    The number of characters written in file.
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
