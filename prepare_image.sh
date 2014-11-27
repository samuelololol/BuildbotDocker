#!/bin/bash
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
ID_FILE=$SOURCE_DIR"/bbd.id"
BBD_DIR=$SOURCE_DIR"/buildbot"

IMAGE_NAME="bbd_img"

CONTAINER_NAME="bbd"
HOST_BDD_PORT=8010
CLIENT_MOUNT_POINT="/buildbot"

docker build -t $IMAGE_NAME .
IMAGE_ID=`docker images | grep $IMAGE_NAME | awk '{print $3}'`

echo ""
echo "BuildBotDocker Image Name: "$IMAGE_NAME
echo "BuildBotDocker Image ID: "$IMAGE_ID
echo ""

