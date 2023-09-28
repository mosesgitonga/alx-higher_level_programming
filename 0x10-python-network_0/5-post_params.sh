#!/bin/bash
#post request to display body of response
curl -s POST -d "{email: test@gmail.com}, {subject: I will always be here for PLD}" "$1"
