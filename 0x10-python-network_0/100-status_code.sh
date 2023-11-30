#!/bin/bash
# Scripts that Sends a request to a URL passed as an argument,displays the status code
curl -s -o /dev/null -w "%{http_code}" "$1"
