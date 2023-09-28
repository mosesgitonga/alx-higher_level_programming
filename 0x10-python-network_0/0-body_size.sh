#!/usr/bin/env bash
#displaying the size of body response

url="$1"
response=$(curl -s -o /dev/null -w "%{size_download}" "$url")
echo "$response"