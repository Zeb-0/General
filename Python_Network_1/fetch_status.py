'''#!/usr/bin/python'''
'''
fetch https://alx-intranet.hbtn.io/status
Usage: ./5-hbtn_header.py <URL>
'''
import requests


if __name__ == '__main__':
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:&')
    print('\t- type: {}$'.format(type(req.text)))
    print('\t-content: {} OK$'.format(req.text))