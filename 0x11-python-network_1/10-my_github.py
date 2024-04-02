#!/usr/bin/python3
"""
Script that takes your GitHub credentials (username and password)
"""

import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
            'https://api.github.com/user', auth=(username, password)
            )
    try:
        user_data = response.json()
        print(user_data.get('id'))
    except ValueError:
        print(None)
