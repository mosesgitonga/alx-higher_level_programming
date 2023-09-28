#!/usr/bin/env bash
#displaying the size of body response
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")
echo "$response"