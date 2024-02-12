'''#!/usr/bin/python'''
'''sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.'''
import sys
import requests


if __name__ == "__main__":
    req = requests.get(sys.argv[1])

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)