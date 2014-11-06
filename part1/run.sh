#!/bin/bash
# A helper script for building and running this image

IMAGE_NAME="chadevs/ipython:latest"

docker build -t ${IMAGE_NAME} .

open http://192.168.59.103:8000

docker run -it -v $(pwd):/var/www/ipython/ --name ipython -p 8000:8000 ${IMAGE_NAME}
