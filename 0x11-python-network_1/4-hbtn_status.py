#!/usr/bin/python3
# Script fetches URL
import requests
url = 'https://intranet.hbtn.io/status'
response = requests.get(url)
print('Body response:')
print('\t - type:', type(response.text))
print ('\t - content:', response.text)
