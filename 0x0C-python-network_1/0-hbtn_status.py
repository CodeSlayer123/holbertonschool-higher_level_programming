#!/usr/bin/python3
if __name__ == "__main__":
    import urllib.request

    a = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('UTF8')))
