#!/usr/bin/env bash
#displaying the size of body response
curl -s "$1" | wc -c