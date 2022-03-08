#!/usr/bin/python3
"""sends POST request to passed URL with email as parameter"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('UTF-8)')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
    print(the_page.decode('UTF8'))
