BuildbotDocker
==============

An buildbot CI environment, its goal is helping developer working with a tiny
but powerful CI system. With every commits pushed, buildbot is triggered new
build and records the test result on master portal.

># Basic CI deployment:
>Prepared docker-composed.yml script will deploy a very simple CI environment.

![basic deployment][1]

># With dockerized test plan:
>Users are able to add their custom dockerized test plan.

![CI_with test deployment][2]

># Triggered by commit pushed:
> Recreate containers for test every build.

![triggered deployment][3]

Requirement
-----------

* Docker
* Docker-compose
* ssh-keys(optional if you're using private repository)
* Platform: Linux (only tested on Linux)

How it works
------------

The prepared docker-compose.yml uses pre-built docker image and mounts host docker.sock to enable creating container from container.


* Dockfiles:
  [master](https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/docker-buildbot/ubuntu-buildbot-master/Dockerfile),
  [slave](https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/docker-buildbot/ubuntu-buildbot-slave/Dockerfile)
* Docker images:
  [samuelololol/ubuntu-buildbot-base](https://hub.docker.com/r/samuelololol/ubuntu-buildbot-base/)
* Docker-compose scritps:
  [docker-compose.yml](https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/docker-buildbot/docker-compose.yml)
* Buildbot config:
  [master.cfg](https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/docker-buildbot/ubuntu-buildbot-master/master.cfg)

Launch Buildbot CI
-----------------

> Download 

    $ wget -O /tmp/master.zip \
          https://github.com/samuelololol/BuildbotDocker/archive/master.zip

> Copy files into your git repository

    $ unzip /tmp/master.zip -d /tmp
    $ cp -r /tmp/BuildbotDocker-master/docker-buildbot/ <YOUR REPO PATH>

> Start Buildbot CI container

    $ cd <YOUR REPO PATH>
    $ docker-compose build && docker-compose up -d


[1]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot.png
[2]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot_test.png
[3]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot_trigger.png
