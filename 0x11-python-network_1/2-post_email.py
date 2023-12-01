#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""
import urllib.request
from sys import argv


def func(argv):
    """
    Method that sends a POST request to the passed URL with
    the email as a parameter,and displays the body of the
    response
    """
    argument = {'email': argv[2]}
    data = urllib.parse.urlencode(argument)
    data = data.encode('utf8')
    link = argv[1]
    send = urllib.request.Request(link, data)
    with urllib.request.urlopen(send) as answer:
        result = answer.read()
        print(result.decode('utf8'))


if __name__ == "__main__":
    func(argv)
