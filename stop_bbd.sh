#!/bin/bash
SOURCE_DIR="${BASH_SOURCE[0]}"
SOURCE_DIR=$(dirname $SOURCE_DIR)
ID_FILE=$SOURCE_DIR"/bbd.id"
BBD_ID=`cat $ID_FILE`
docker stop $BBD_ID
docker rm $BBD_ID
rm -rf $ID_FILE

