#!/bin/bash
# Send a GET request to URL, get the status code
curl -s -o /dev/null -w "%{http_code}" "$1"