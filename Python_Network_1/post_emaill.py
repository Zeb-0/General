'''#!/usr/bin/python3'''
'''
Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
displays the body of the response (decoded in utf-8)
'''

import urllib.parse
import sys
import urllib.request

if __name__ == '__main__':
    '''Get Url and email from command line arguments'''
    url = sys.argv[1]
    value = sys.argv[2]

    '''Encode the email'''
    data = urllib.parse.urlencode({"email": value}).encode("ascii")
    '''Send POST request'''
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        # Read and decode response
        print(response.read().decode('utf-8'))