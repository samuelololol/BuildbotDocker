BuildbotDocker
==============

An Easy CI environment for development. Built from custom buildbot in docker image. 

1. Master/slave configs for a git-repo project
2. commit-triggered built
3. Composed of multiple container for full CI set
4. [nice to have] deployment with docker container by docker API


Requirement
----------
* [Docker-1.3.2](://github.com/docker/docker/blob/v1.3.2/CHANGELOG.md#132-2014-11-20)
* [samuelololol/gentoo-buildbot:0.9](https://registry.hub.docker.com/u/samuelololol/gentoo-buildbot/tags/manage/)
* Git



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

