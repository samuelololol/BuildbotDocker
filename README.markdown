BuildbotDocker
==============

An buildbot CI environment for developing.

># Basic CI deployment:
>Prepared docker-composed.yml script will deploy a very simple CI environment.

![basic deployment][1]

># With dockerized test plan:
>Users are able to add their custom dockerized test plan

![CI_with test deployment][2]

Requirement
-----------

* Docker
* Docker-compose
* ssh-keys(optional if you're using private repository)
* only tested on Linux

Launch Buildbot CI
---

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
