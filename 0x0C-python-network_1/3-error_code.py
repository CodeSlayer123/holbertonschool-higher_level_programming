#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('UTF8'))
    except urllib.error.HTTPError as e:
            print("Error code: {}".format(e.code))
