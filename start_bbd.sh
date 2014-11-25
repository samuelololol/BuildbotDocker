#!/bin/bash
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"
ID_FILE=$SOURCE_DIR"/bbd.id"
BBD_DIR=$SOURCE_DIR"/buildbot"

CONTAINER_NAME="bbd"
HOST_BDD_PORT=8011
CLIENT_MOUNT_POINT="/buildbot"


CONTAINER_ID=`docker run -d --name bbd -p $HOST_BDD_PORT:8010 -v $BBD_DIR:$CLIENT_MOUNT_POINT samuelololol/gentoo-buildbot`
echo $CONTAINER_ID > $ID_FILE

