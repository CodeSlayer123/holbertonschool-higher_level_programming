#!/usr/bin/python3
"""sends a request to the URL and displays the value of variable"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.info()
    x = html.get("X-Request-Id")
    print(x)
