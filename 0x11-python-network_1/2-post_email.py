#!/usr/bin/python3
# Script takes in URL and email, sends POST request, &displays body of response
import urllib.parse
import urllib.request
import sys
url = sys.argv[1]
values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page.decode('utf-8'))