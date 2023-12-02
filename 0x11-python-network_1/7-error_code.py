#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response. If the HTTP status code
is greater than or equal to 400, print: Error code: followed by
the value of the HTTP status code
"""

import requests
from sys import argv


def func(argv):
    """
    Method that checks If the HTTP status code is greater than
    or equal to 400, print: Error code
    """
    link = argv[1]
    req = requests.get(link)
    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        print("Error code: {}".format(req.status_code))


if __name__ == "__main__":
    func(argv)
