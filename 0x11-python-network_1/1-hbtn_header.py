#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
from sys import argv


def func(argv):
    """
    Method that displays the value of the X-Request-Id variable
    found in the header of the response
    """
    link = argv
    with urllib.request.urlopen(link) as answer:
        headers = answer.info()
        print(headers['X-Request-Id'])


if __name__ == "__main__":
    func(argv[1])
