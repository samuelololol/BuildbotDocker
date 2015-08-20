BuildbotDocker
==============

An buildbot CI environment, its goal is helping developer working with a tiny
but powerful CI system. With every commits pushed, buildbot is triggered new
build and records the test result on master portal.

># Basic CI deployment:
>Using prepared docker-composed.yml script to deploy a very simple CI environment.

![basic deployment][1]

># With dockerized test plan:
>Buildbot Slave has ability to create containers(on host) as well, so users could 
execute their custom dockerized test plan.

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

How to use
----------
Download, edit and run.

### Settings
* master.cfg
* buildbotdocker.py

These 2 files are main core settings for buildbot. The complicated settings are extracted separately from original `master.cfg` into `master.cfg` and `buildbotdocker.py`. To edit the settings, it is necessary for you to consider some aspects:

1. Deploy scenario: Add deployment steps into builder. It is recommanded using Docker to reproduce clean target environment and to setup the project.
2. Test scenario: Add test runner scripts into builder. It is depending on how the project do tests. You are able to launch test runner on buildbot slave or do it on clean Docker container(s).

How to launch
-------------

![under construction.][4]

<!---
> Download 

    $ wget -O /tmp/master.zip \
          https://github.com/samuelololol/BuildbotDocker/archive/master.zip

> Copy files into your git repository

    $ unzip /tmp/master.zip -d /tmp
    $ cp -r /tmp/BuildbotDocker-master/docker-buildbot/ <YOUR REPO PATH>

> Start Buildbot CI container

    $ cd <YOUR REPO PATH>
    $ docker-compose build && docker-compose up -d
-->


[1]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot.png
[2]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot_test.png
[3]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot_trigger.png

[4]: http://images.all-free-download.com/images/graphiclarge/free_urban_background_48269.jpg
