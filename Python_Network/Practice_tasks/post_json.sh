#!/bin/bash
# post a json file to url
curl -s -X POST -H "content-type: application/json" -d "$(cat $2)" "$1"