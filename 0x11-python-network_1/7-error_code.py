#!/usr/bin/python3
# script takes in URL, sends request, returns error code or body response
import requests
import sys
url = sys.argv[1]
response = requests.get(url)
if response.status_code > 400:
    print('Error code:', response.status_code)
else:
    print(response.text)
