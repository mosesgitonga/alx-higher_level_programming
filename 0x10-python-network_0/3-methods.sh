#!/bin/bash
#get allowed headers
curl -sI "$1" | grep -i "Allow" | cut -d " " -f 2-
