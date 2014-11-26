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
CONTAINER_ID=`docker run -d --name bbd -p $HOST_BDD_PORT:8010 -v $BBD_DIR:$CLIENT_MOUNT_POINT $IMAGE_NAME`
echo $CONTAINER_ID > $ID_FILE
echo "bbd sha1: "$CONTAINER_ID
echo ""
echo "To enter the container:"
echo "docker exec -it $CONTAINER_ID" bash
echo ""

