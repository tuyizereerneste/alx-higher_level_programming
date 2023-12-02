#!/usr/bin/python3
"""script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter
displays the body of the response
"""

import requests
from sys import argv


def func(argv):
    """Method that sends a POST request to the passed URL
    with the email as a parameter, displays the body of the response
    """

    argument = {'email': argv[2]}
    link = argv[1]
    req = requests.post(link, data=argument)
    print(req.text)


if __name__ == "__main__":
    func(argv)
