#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL.
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
