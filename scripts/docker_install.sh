#!/bin/bash
set -e

echo "Updating packages..."
sudo apt-get update -y || sudo yum update -y

echo "Installing Docker..."
if [ -x "$(command -v yum)" ]; then
    sudo yum install -y docker
elif [ -x "$(command -v apt-get)" ]; then
    sudo apt-get install -y docker.io
else
    echo "Unsupported package manager. Install Docker manually."
    exit 1
fi

echo "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker
