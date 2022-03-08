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
    if len(r) == 0:
        print("No result")
    else:
        try:
            jason = r.json()
            print("[{}] {}".format(r.id, r.name))
        except:
            print("Not a valid JSON")
