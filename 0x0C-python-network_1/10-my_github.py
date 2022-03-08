#!/usr/bin/python3
"""takes GitHub credentials and uses  GitHub API to display id"""

if __name__ == "__main__":

    import requests
    import sys

    user = sys.argv[1]
    pswd = sys.argv[2]
    url = f"https://api.github.com/users/{user}"

    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, pswd)).json()
    print(r.get('id'))
