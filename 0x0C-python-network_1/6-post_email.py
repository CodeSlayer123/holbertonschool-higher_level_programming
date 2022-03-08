#!/usr/bin/python3
"""sends POST request to  passed URL with  email as parameter"""

if __name__ == "__main__":
    import requests
    import sys

    a = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(a, data=payload)
    print(r.text)
