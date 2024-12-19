#!/bin/bash
set -e

echo "Updating packages..."
if [ -x "$(command -v yum)" ]; then
    sudo yum update -y
elif [ -x "$(command -v apt-get)" ]; then
    sudo apt-get update -y
else
    echo "Unsupported package manager. Update manually."
    exit 1
fi

echo "Checking if Docker is already installed..."
if ! [ -x "$(command -v docker)" ]; then
    echo "Installing Docker..."
    if [ -x "$(command -v yum)" ]; then
        sudo yum install -y docker
    elif [ -x "$(command -v apt-get)" ]; then
        sudo apt-get install -y docker.io
    fi
else
    echo "Docker is already installed."
fi

echo "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker
