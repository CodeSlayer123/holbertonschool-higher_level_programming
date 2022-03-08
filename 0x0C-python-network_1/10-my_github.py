#!/usr/bin/python3
"""takes GitHub credentials and uses  GitHub API to display id"""

if __name__ == "__main__":

    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    user = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(user, token)).json()
    print(r.get('id'))
