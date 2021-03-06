#!/usr/bin/python3
"""takes GitHub credentials and uses  GitHub API to display id"""

if __name__ == "__main__":

    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    url = "https://api.github.com/user"

    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2])).json()
    print(r.get('id'))
