#!/usr/bin/python3
# Script fetches URL
import requests
if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print('Body response:')
    print('\t - type:', type(response.text))
    print ('\t - content:', response.text)
