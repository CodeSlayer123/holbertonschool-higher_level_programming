#!/usr/bin/python3
import urllib.request


if __name__ == "__main__":
    a = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('UTF8')))