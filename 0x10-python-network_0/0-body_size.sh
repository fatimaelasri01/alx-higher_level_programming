#!/bin/bash
# sends a request to an URL and displays the size of the body of the response
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
