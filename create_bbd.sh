#!/bin/bash
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
ID_FILE=$SOURCE_DIR"/bbd.id"

IMAGE_NAME="bbd_img"
CONTAINER_NAME=$(cat /dev/urandom | tr -dc 'A-Z0-9' | fold -w 10 | head -n 1)
HOST_BDD_PORT=8010
IMAGE_ID=`docker images | grep $IMAGE_NAME | awk '{print $3}'`


if [ "$#" -eq 2 ]; then
    echo ""
    echo "use $1 as image name"
    echo "use $2 as buildbot port"
    IMAGE_NAME=$1
    HOST_BDD_PORT=$2
elif [ "$#" -eq 1 ]; then
    echo ""
    echo "Usage:    $ ./create_bbd.sh <bbd image name> [<buildbot portal port>]"
    echo ""
    echo "use $1 as image name"
    echo "use default buildbot port 8010"
else
    echo ""
    echo "Usage:    $ ./create_bbd.sh <bbd image name> [<buildbot portal port>]"
    echo ""
    exit 42
fi

CONTAINER_ID=`docker run -d -v /var/run/docker.sock:/var/run/docker.sock --name $CONTAINER_NAME -p $HOST_BDD_PORT:8010 $IMAGE_NAME`

if [ "$?" -ne 0 ]; then
    echo ""
    echo "[ERROR] create container fail"
    exit 43
fi

echo "$CONTAINER_ID $CONTAINER_NAME"> $ID_FILE
echo "$CONTAINER_NAME sha1: "$CONTAINER_ID
echo ""
echo "To enter the container($CONTAINER_NAME):"
echo ""
echo "$ docker exec -it $CONTAINER_ID" bash
echo "OR"
echo "$ docker exec -it $CONTAINER_NAME" bash
echo ""

