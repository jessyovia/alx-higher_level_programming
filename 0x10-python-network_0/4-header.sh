#!/bin/bash

# This script sends a GET request to a URL with a specific header and displays the body of the response.

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send a GET request with the specified header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$url"
