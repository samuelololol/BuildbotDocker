#!/bin/bash
SOURCE_DIR="${BASH_SOURCE[0]}"
SOURCE_DIR=$(dirname $SOURCE_DIR)
ID_FILE=$SOURCE_DIR"/bbd.id"
BBD_ID=$(cat bbd.id | tr -s " " "\012" | head -n 1)
docker stop $BBD_ID
docker rm $BBD_ID
rm -rf $ID_FILE

