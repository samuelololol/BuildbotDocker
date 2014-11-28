#!/bin/bash
IMAGE_NAME="bbd_img"
docker images | grep $IMAGE_NAME | awk '{print $3}' | xargs docker rmi

