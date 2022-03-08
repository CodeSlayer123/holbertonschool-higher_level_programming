#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status only using requests"""

if __name__ == "__main__":
    import urllib.request

    a = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
