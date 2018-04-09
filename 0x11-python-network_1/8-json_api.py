#!/usr/bin/python3
# script takes in a letter, sends post request,&evaluates whether json or not
import sys
import requests
if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        q_val = ""
    else:
        q_val = sys.argv[1]
        response = requests.post(url, data={'q': q_val})
    if len(response.json()) != 0:
        try:
            data = response.json()
            data_id = '[' + str(data['id']) + ']'
            print(data_id, end=" ")
            print(data['name'])
        except ValueError:
            print('Not a valid JSON')
    else:
        print('No result')
