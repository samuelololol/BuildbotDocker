#!/bin/bash
IMAGE_NAME="bbd_img"
IMAGE_ID=`docker images | grep $IMAGE_NAME | awk '{print $3}'`
docker rmi $IMAGE_ID

