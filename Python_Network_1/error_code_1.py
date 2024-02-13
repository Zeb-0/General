'''#!/usr/bin/python'''
'''Display error message and code'''
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)