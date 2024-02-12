'''#!/usr/bin/python'''
'''fetch https://alx-intranet.hbtn.io/status'''
import requests

req = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:&')
print('\t- type: {}$'.format(type(req.text)))
print('\t-content: {} OK$'.format(req.text))