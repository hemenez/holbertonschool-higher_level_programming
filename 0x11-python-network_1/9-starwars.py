#!/usr/bin/python3
# script searches Star Wars API by taking in a string via CL
import sys
import requests
url = 'https://swapi.co/api/people/?'
desired_url = url + 'search=' + sys.argv[1]
response = requests.get(desired_url)
data = response.json()
data = dict(data)
print('Number of results:', data['count'])
for k in data['results']:
    print(k['name'])
