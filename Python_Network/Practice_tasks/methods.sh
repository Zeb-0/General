#!/bin/bash
#display all the methods allowed by a server

curl -siX OPTIONS "$1"
