'''#!/usr/bin/python'''
'''Use requests to display value of the variable `X-Request-Id` in the response headers'''
import sys
import requests

req = requests.get(sys.argv[1])