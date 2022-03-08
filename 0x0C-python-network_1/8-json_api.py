#!/usr/bin/python3
"""takes in URL, sends request to URL & displays body of response"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    a = 'http://0.0.0.0:5000/search_user'
    payload = {'letter': q}
    r = requests.post(a, data=payload)

    try:
        jason = r.json()
        if len(jason) == 0:
            print("No result")
        else:
            print("[{}] {}".format(jason['id'], jason['name']))
    except Exception:
        print("Not a valid JSON")
