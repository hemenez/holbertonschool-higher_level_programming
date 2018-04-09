#!/usr/bin/python3
# Script takes in URL and displays request value id found in header
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        data = response.getheaders()
        data = dict(data)
        print(data['X-Request-Id'])
