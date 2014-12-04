BuildbotDocker
==============

An Easy CI environment for development. Built from custom buildbot in docker image. 

1. Master/slave configs for a git-repository project
2. Commit-triggered built
3. Composed of multiple container for full CI set
4. [nice to have] deployment with docker container by docker API


Requirement
-----------
* [Docker-1.3.2](http://github.com/docker/docker/blob/v1.3.2/CHANGELOG.md#132-2014-11-20)
* Buildbot Docker image: [samuelololol/gentoo-buildbot:0.8](https://registry.hub.docker.com/u/samuelololol/gentoo-buildbot/tags/manage/), which contains:
  * 1 master/ 1 slave installed
  * Deployment is described by [Dockerfile](https://github.com/samuelololol/BuildbotDocker/blob/master/Dockerfile)
* Using privilege repository, prepare SSH key(private/public keys, which have been [ignored from repository](https://github.com/samuelololol/BuildbotDocker/blob/master/.gitignore#L57)), add manually under the path: [buildbot/bin](https://github.com/samuelololol/BuildbotDocker/tree/master/buildbot/bin)
```
      BuildbotDocker/buildbot/bin:
        ..
        -rw------- 1 buildbot buildbot 1679 Nov 13 03:17 id_rsa
        -rwxrwxrwx 1 buildbot buildbot  399 Nov 13 15:38 id_rsa.pub
```

Install and Setup
-----------------
1. Install git/docker
2. $ git pull https://github.com/samuelololol/BuildbotDocker.git
3. Edit configs
  1. [buildbot/master.cfg](https://github.com/samuelololol/BuildbotDocker/blob/master/buildbot/master.cfg): master settings(repository path/branch name)
  2. (Recommanded) [create_bbd.sh](https://github.com/samuelololol/BuildbotDocker/blob/master/create_bbd.sh): container settings(buildbot portal port)
  1. (Optional) [prepare_image.sh](https://github.com/samuelololol/BuildbotDocker/blob/master/prepare_image.sh): image settings(image name), or assign prepared-buildbot folder
  4. (Optional) dockerfile.diff: A diff file in order to append to [Dockerfile](https://github.com/samuelololol/BuildbotDocker/blob/master/Dockerfile)
  5. (Optional) Prepare ssh keys to [buildbot/bin](https://github.com/samuelololol/BuildbotDocker/tree/master/buildbot/bin) folder if using any privilege repository
4. $ ./prepare_image.sh &lt;buildbot folder path&gt; [&lt;dockerfile.diff&gt;]
5. $ ./create_bbd.sh &lt;bbd image name&gt; [&lt;buildbot portal port&gt;]
6. Links to [buildbot portal(http://127.0.0.1:8010/)](http://127.0.0.1:8010/)

Delete container or Remove image
----------------------
* ./delete_bbd.sh: remove bbd container recorded in bbd.id file
* ./remove_images.sh: remove all bbd images

Resources
---------
* [Buildbot](http://buildbot.net)
* [Docker.com](https://www.docker.com/)
  * [docker-py Documentation](http://docker-py.readthedocs.org/en/latest/)
  * [Docker cheat-sheep](https://github.com/wsargent/docker-cheat-sheet)
  * [Docker Remote API](http://docs.docker.com/reference/api/docker_remote_api_v1.9/), The daemon listens on unix:///var/run/docker.sock but you can bind Docker to another host/port or a Unix socket.
* [Buildbot docker image in Gentoo](https://registry.hub.docker.com/u/samuelololol/gentoo-buildbot/)
* Slides
  * [Continuous integration with docker, buildbot and git](http://www.slideshare.net/Adieu/continuous-integration-with-docker-buildbot-and-git)
  * [Buildbot in Docker](http://slidedeck.io/mboersma/buildbot-docker-presentation)

