#!/usr/bin/python3
"""package requests that fetches https://alx-intranet.hbtn.io/status"""
import requests


def func():
    """Method that fetches https://alx-intranet.hbtn.io/status
    using requests package
    """
    link = 'https://intranet.hbtn.io/status'
    req = requests.get(link)
    print('Body response:')
    print('\t- type: {}'.format(type(req.text)))
    print('\t- content: {}'.format(req.text))


if __name__ == "__main__":
    func()
