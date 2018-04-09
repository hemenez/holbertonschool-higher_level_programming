#!/usr/bin/python3
# script takes GitHub credentials and displays user's id
import requests
import sys
user = sys.argv[1]
passwd = sys.argv[2]
url = 'https://api.github.com/user'
response = requests.get(url, auth=(user, passwd))
data = response.json()
data = dict(data)
try:
    print(data['id'])
except KeyError:
    print('None')
