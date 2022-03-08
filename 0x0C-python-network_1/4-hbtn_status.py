#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status only using requests"""

if __name__ == "__main__":
    import requests

    a = 'https://intranet.hbtn.io/status'
    html = requests.get(a)
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
