FROM samuelololol/ubuntu-buildbot-base
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN ["buildslave", "create-slave", "--umask=022", "/app", "buildbotmaster:9989", "example-slave", "pass"]
CMD ["buildslave", "start", "--nodaemon", "/app"]

