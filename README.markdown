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

How it works[TDB]
------------

* Dockfiles
* Docker images
* Docker-compose scritps
* Buildbot config

Launch Buildbot CI
-----------------

> Download 

    $ wget https://github.com/samuelololol/BuildbotDocker/archive/master.zip
    $ unzip master.zip -d /tmp

> Copy files into your git repository

    $ cp -r /tmp/BuildbotDocker-master/docker-buildbot/ <YOUR REPO PATH>

> Start Buildbot CI container

    $ cd <YOUR REPO PATH>
    $ docker-compose build && docker-compose up -d


[1]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot.png
[2]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot_test.png
[3]: https://raw.githubusercontent.com/samuelololol/BuildbotDocker/master/.diagram/buildbot_trigger.png
