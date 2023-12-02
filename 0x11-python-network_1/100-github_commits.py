#!/usr/bin/python3
"""
script that takes 2 arguments in order toaccess
the GitHub API and uses the information
"""

import requests
from requests.auth import HTTPBasicAuth
from sys import argv


def func(argv):
    """
    Method that list 10 commits by takeing 2 arguments
    The first argument will be the repository name
    The second argument will be the owner nam
    """

    def print_commits(i, commit_list):
        """function that prints 10 commits"""
        sha = commit_list[i].get('sha')
        commit = commit_list[i].get('commit')
        author = commit.get('author')
        name = author.get('name')
        print('{}: {}'.format(sha, name))
    repo = argv[1]
    owner = argv[2]
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get('https://api.github.com/repos/' + owner +
                            '/' + repo + '/commits', headers=headers)
    commit_list = response.json()
    size = len(commit_list)
    if size < 10:
        for i in range(0, size):
            print_commits(i, commit_list)
        else:
            for i in range(0, 10):
                print_commits(i, commit_list)


if __name__ == "__main__":
    func(argv)
