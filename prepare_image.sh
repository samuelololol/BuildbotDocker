#!/bin/bash
SOURCE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}"  )" && pwd  )"

if [ "$#" -ne 1 ]; then
    echo ""
    echo "./prepare_image.sh <buildbot folder path>"
    echo ""
    echo "use default buildbot setting:"
    echo "  $SOURCE_DIR/buildbot"
else
    echo ""
    echo "use $1 as buildbot folder"

    rm -rf $SOURCE_DIR/buildbot
    BUILDBOT_FDR=$1
    local_bbd_fdr_name=${1%/}
    local_bbd_fdr_name=${local_bbd_fdr_name##*/}
    if [[ -d $1 ]]; then
        cp -r $1 .
        if [ "$local_bbd_fdr_name" != "buildbot" ]; then
            mv $local_bbd_fdr_name buildbot
        fi
    else
        exit 1
    fi
fi

IMAGE_NAME="bbd_img"
docker build -t $IMAGE_NAME .
IMAGE_ID=`docker images | grep $IMAGE_NAME | awk '{print $3}'`

echo ""
echo "BuildBotDocker Image Name: "$IMAGE_NAME
echo "BuildBotDocker Image ID: "$IMAGE_ID
echo ""

