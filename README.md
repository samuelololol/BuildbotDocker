BuildbotDocker
==============

An Easy CI environment for development. Built from custom buildbot in docker image. 

1. Master/slave configs for a git-repo project
2. Commit-triggered built
3. Composed of multiple container for full CI set
4. [nice to have] deployment with docker container by docker API


Requirement
-----------
* [Docker-1.3.2](http://github.com/docker/docker/blob/v1.3.2/CHANGELOG.md#132-2014-11-20)
* Buildbot Docker image: [samuelololol/gentoo-buildbot:0.9](https://registry.hub.docker.com/u/samuelololol/gentoo-buildbot/tags/manage/), which contains:
  * 1 buildmaster/ 1 buildslave installed
  * Deployment is described by [Dockerfile](https://github.com/samuelololol/BuildbotDocker/blob/master/Dockerfile)
  * Git, if the repository protocol is ssh://, prepare SSH key(private/public keys, which have been [ignored from repo](https://github.com/samuelololol/BuildbotDocker/blob/master/.gitignore#L57)), add manually under repo path: [buildbot/bin](https://github.com/samuelololol/BuildbotDocker/tree/master/buildbot/bin)
```
      BuildbotDocker/buildbot/bin:
        ..
        -rw------- 1 buildbot buildbot 1679 Nov 13 03:17 id_rsa
        -rwxrwxrwx 1 buildbot buildbot  399 Nov 13 15:38 id_rsa.pub
```

Install and Setup
-----------------
1. install git/docker
2. $ git pull https://github.com/samuelololol/BuildbotDocker.git
3. edit configs
  1. [Dockerfile](https://github.com/samuelololol/BuildbotDocker/blob/master/Dockerfile): Docker image setting
  2. [prepare_image.sh](https://github.com/samuelololol/BuildbotDocker/blob/master/prepare_image.sh): image settings
  3. [create_bbd.sh](https://github.com/samuelololol/BuildbotDocker/blob/master/create_bbd.sh): container settings
  4. [buildbot/master.cfg](https://github.com/samuelololol/BuildbotDocker/blob/master/buildbot/master.cfg): master settings
  5. (Optional) prepare ssh keys to [buildbot/bin](https://github.com/samuelololol/BuildbotDocker/tree/master/buildbot/bin)
4. $ ./prepare_image.sh
5. $ ./create_bbd.sh
6. link to [buildbot portal(http://127.0.0.1:8010/)](http://127.0.0.1:8010/)

Delete or Remove Image
----------------------
* ./delete_bbd.sh
* ./remove_image.sh

Resources
---------
* [Buildbot](http://buildbot.net)
* [Docker.com](https://www.docker.com/)
  * [Docker cheat-sheep](https://github.com/wsargent/docker-cheat-sheet)
  * [Docker Remote API](http://docs.docker.com/reference/api/docker_remote_api_v1.9/), The daemon listens on unix:///var/run/docker.sock but you can bind Docker to another host/port or a Unix socket.
* [Buildbot docker image in Gentoo](https://registry.hub.docker.com/u/samuelololol/gentoo-buildbot/)
* Slides
  * [Continuous integration with docker, buildbot and git](http://www.slideshare.net/Adieu/continuous-integration-with-docker-buildbot-and-git)
  * [Buildbot in Docker](http://slidedeck.io/mboersma/buildbot-docker-presentation)

