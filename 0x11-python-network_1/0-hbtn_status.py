#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""

import urllib.request


def func():
    """print a response of a specific url"""
    link = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(link) as answer:
        html = answer.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf8')))


if __name__ == "__main__":
    func()
