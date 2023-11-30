#!/bin/bash
# displays the size of the body of the response.
URL="$1"
curl -sI "$URL" | awk '/Content-Length/{print $2}'
