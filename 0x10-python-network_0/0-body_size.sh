#!/bin/bash
# script to check size of the response in bytes
curl -s "$1" | wc -c
