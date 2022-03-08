#!/usr/bin/python3
"""takes in URL, sends request to URL & displays body of response"""

if __name__ == "__main__":
    import requests
    import sys

    a = sys.argv[1]
    r = requests.get(a)
    if r.ok is False:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
