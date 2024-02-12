'''#!/usr/bin/python'''
'''displays the value of the X-Request-Id variable found in the header of the response.'''

import sys
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(reg) as response:
        print(dict(response.headers).get('X-Request-Id'))
