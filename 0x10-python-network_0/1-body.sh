#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response

response=$(curl -sI "$1" | grep "200" | cut -d " " -f2)
if [[ "$response" =~ ^[0-9]+$ ]]; then
	if [ "$response" -eq 200 ]; then
  		curl -s "$1"
	fi
fi
