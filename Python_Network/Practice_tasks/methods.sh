#!/bin/bash
#display all the methods allowed by a server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
