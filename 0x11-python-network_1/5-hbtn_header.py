#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id in the response header
"""

import requests
from sys import argv


def func(argv):
    """Method that displays the value of the variable
    X-Request-Id in the response header
    """

    link = argv[1]
    req = requests.get(link)
    headers = req.headers.get('X-Request-Id')
    print(headers)


if __name__ == "__main__":
    func(argv)
