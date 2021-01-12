#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of the repository ."""

if __name__ == "__main__":
    import requests
    from sys import argv
    repository = argv[1]
    owner = argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner,
                                                              repository)
    response = requests.get(url)
    commits = response.json()[:10]
    for commit in commits:
        author = commit.get('commit').get('author').get('name')
        sha = commit.get('sha')
        print('{}: {}'.format(sha, author))
