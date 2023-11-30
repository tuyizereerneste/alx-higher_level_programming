#!/bin/bash
# Scripts that send JSON POST request to a URL passed as the first argument,displays body of the response.
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
