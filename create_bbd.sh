#!/bin/bash
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
ID_FILE=$SOURCE_DIR"/bbd.id"

IMAGE_NAME="bbd_img"
CONTAINER_NAME=$(cat /dev/urandom | tr -dc 'A-Z0-9' | fold -w 10 | head -n 1)
HOST_BDD_PORT=8010
IMAGE_ID=`docker images | grep $IMAGE_NAME | awk '{print $3}'`

CONTAINER_ID=`docker run -d --name $CONTAINER_NAME -p $HOST_BDD_PORT:8010 $IMAGE_NAME`

echo "$CONTAINER_ID $CONTAINER_NAME"> $ID_FILE
echo "$CONTAINER_NAME sha1: "$CONTAINER_ID
echo ""
echo "To enter the container($CONTAINER_NAME):"
echo "docker exec -it $CONTAINER_ID" bash
echo ""

