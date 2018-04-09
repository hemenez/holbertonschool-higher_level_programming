#!/usr/bin/python3
# Script takes in URL, sends request to it, &displays body of response
import sys
import urllib.request
import urllib.error
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
