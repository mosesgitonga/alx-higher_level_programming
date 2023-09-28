#!/bin/bash
#script that returns the body of a response
response=$(curl -s -w "%{http_code}" "$1"); 
[ "${response: -3}" -eq 200 ] && echo "$response" 