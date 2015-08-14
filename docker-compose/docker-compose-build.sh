#!/bin/bash

mkdir -p ubuntu-buildbot-master ubuntu-buildbot-slave
wget -O ubuntu-buildbot-master/Dockerfile https://raw.githubusercontent.com/samuelololol/mydockerfiles/master/ubuntu-buildbot-master/Dockerfile
wget -O ubuntu-buildbot-master/master.cfg https://raw.githubusercontent.com/samuelololol/mydockerfiles/master/ubuntu-buildbot-master/master.cfg
wget -O ubuntu-buildbot-slave/Dockerfile https://raw.githubusercontent.com/samuelololol/mydockerfiles/master/ubuntu-buildbot-slave/Dockerfile
docker-compose build

