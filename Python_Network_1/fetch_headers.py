'''#!/usr/bin/python'''
'''Use requests to display value of the variable `X-Request-Id` in the response headers'''
import sys
import requests


if __name__ == '__main__':
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))