#!/usr/bin/python3
"""package requests that fetches https://alx-intranet.hbtn.io/status"""
import requests


def func():
    """Method that fetches https://alx-intranet.hbtn.io/status
    using requests package
    """
    link = 'https://intranet.hbtn.io/status'
    request = requests.get(link)
    print('Body response:')
    print('\t- type: {}'.format(type(request.text)))
    print('\t- content: {}'.format(request.text))


if __name__ == "__main__":
    func()
