#!/bin/bash
SOURCE_DIR="${BASH_SOURCE[0]}"
SOURCE_DIR=$(dirname $SOURCE_DIR)
ID_FILE=$SOURCE_DIR"/bbd.id"
CONTAINER_ID=`docker run -d samuelololol/gentoo-buildbot`
echo $CONTAINER_ID > $ID_FILE
