#!/usr/bin/python3
# Script takes in a URL, sends request, &displays value of variable id
import sys
import requests
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    data = response.headers.get('X-Request-Id')
    print(data)
