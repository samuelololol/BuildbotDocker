#!/bin/bash
#
# date: 2014/12/05
# author: samuel

SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"

if [ "$#" -eq 2 ]; then
    echo ""
    echo "use $1 as buildbot settings"
    echo "add diff of dockerfiles:$2 to Dockerfile"
    echo ""

    if [[ -f $2 ]]; then
        cat $2 >> $SOURCE_DIR/Dockerfile
    else
        echo ""
        echo "[ERROR] $2 is not a regular file"
        exit 42
    fi

elif [ "$#" -eq 1 ]; then
    echo ""
    echo "Usage:    $ ./prepare_image.sh <buildbot folder path> [<dockerfile.diff>]"
    echo ""
    echo "use default buildbot setting:"
    echo "  $SOURCE_DIR/buildbot"
    echo "use default Dockerfile"
else
    echo ""
    echo "Usage:    $ ./prepare_image.sh <buildbot folder path> [<dockerfile.diff>]"
    echo ""
    exit 42
fi


BUILDBOT_FDR=$1
local_bbd_fdr_name=${1%/}
local_bbd_fdr_name=${local_bbd_fdr_name##*/}
if [[ -d $1 ]]; then
    rm -rf $SOURCE_DIR/buildbot
    cp -r $1 .
    if [ "$local_bbd_fdr_name" != "buildbot" ]; then
        mv $local_bbd_fdr_name buildbot
    fi
else
    echo ""
    echo "[ERROR] buildbot setting is not a folder"
    exit 43
fi

DEFAULT_IMAGE_NAME="bbd_img"
IMAGE_NAME=`docker images | grep $DEFAULT_IMAGE_NAME | awk '{print $1}'`
if [ "$IMAGE_NAME" == "" ]; then
    IMAGE_NAME="bbd_img"
else
    RPOSTFIX=$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 10 | head -n 1)
    IMAGE_NAME="bbd_img_"$RPOSTFIX
fi


docker build -t $IMAGE_NAME .
IMAGE_ID=`docker images | grep $IMAGE_NAME | awk '{print $3}'`

echo ""
echo "BuildBotDocker Image Name: "$IMAGE_NAME
echo "BuildBotDocker Image ID: "$IMAGE_ID
echo ""
echo "create container: "
echo "Usage:    $ ./create_bbd.sh $IMAGE_NAME [<buildbot portal port>]"
echo "    OR    $ ./create_bbd.sh $IMAGE_ID [<buildbot portal port>]"

