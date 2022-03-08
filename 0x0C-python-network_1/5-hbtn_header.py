#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status only using requests"""

if __name__ == "__main__":
    import requests
    import sys

    a = sys.argv[1]
    r = requests.get(a)
    print(r.headers.get('X-Request-Id'))
