#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
echo "Pulling Docker image"
docker pull yash1thyerra/sample-python-flask-app

# Run the Docker image as a container
echo "Running Docker image "
docker run -d -p 5000:5000 yash1thyerra/sample-python-flask-app
