BuildbotDocker
==============

An Easy CI environment for development. Built from custom buildbot in docker image. 

1. Master/slave configs for a git-repo project
2. Commit-triggered built
3. Composed of multiple container for full CI set
4. [nice to have] deployment with docker container by docker API


Requirement
----------
* [Docker-1.3.2](http://github.com/docker/docker/blob/v1.3.2/CHANGELOG.md#132-2014-11-20)
* Buildbot Docker image: [samuelololol/gentoo-buildbot:0.9](https://registry.hub.docker.com/u/samuelololol/gentoo-buildbot/tags/manage/)
  * 1 buildmaster/ 1 buildslave installed
  * Configuration files from host(default configuration setting template are located in [this repository](https://github.com/samuelololol/BuildbotDocker/tree/master/buildbot)) are mount at `/buildbot` in container, `/var/lib/buildmaster/master.cfg` is already softlinked from there
  * /var/lib/buildmaster and /var/lib/buildslave

```
      /var/lib/buildmaster: 
        lrwxrwxrwx 1 buildbot buildbot     14 Nov 25 07:14 bin -> /buildbot/bin/
        lrwxrwxrwx 1 buildbot buildbot     29 Nov 25 07:20 buildbot.tac -> /buildbot/buildbot.tac.master
        lrwxrwxrwx 1 buildbot buildbot     20 Nov 25 07:20 master.cfg -> /buildbot/master.cfg
      /var/lib/buildslave:
        lrwxrwxrwx 1 buildbot buildbot     28 Nov 25 07:22 buildbot.tac -> /buildbot/buildbot.tac.slave
```
* Git
  * If the repository protocol is ssh://, prepare SSH key(private/public keys), which have been [ignored from repo](https://github.com/samuelololol/BuildbotDocker/blob/master/.gitignore#L57), add manually with following permission
```
     /var/lib/buildmaster/bin
        -rw------- 1 buildbot buildbot 1679 Nov 13 03:17 id_rsa
        -rwxrwxrwx 1 buildbot buildbot  399 Nov 13 15:38 id_rsa.pub
```

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

