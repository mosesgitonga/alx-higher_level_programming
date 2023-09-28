#!/bin/bash
#script that returns the body of a response
response=$(curl -s -w "%{http_code}" "$1"); if [ "${response: -3}" -eq 200 ]; then echo "$response" 
fi