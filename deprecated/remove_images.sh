#!/bin/bash
#
# date: 2014/12/05
# author: samuel

IMAGE_NAME="bbd_img"
docker images | grep $IMAGE_NAME | awk '{print $3}' | xargs docker rmi

