#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user.
"""

import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(
                json_response.get('id'), json_response.get('name'))
                )
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
