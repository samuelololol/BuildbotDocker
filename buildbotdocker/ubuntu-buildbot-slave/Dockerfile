FROM samuelololol/ubuntu-buildbot-base
MAINTAINER samuelololol <samuelololol@gmail.com>
COPY git_ssh /usr/local/bin/git_ssh
ENV GIT_SSH=/usr/local/bin/git_ssh \
    TZ=Asia/Taipei
RUN ["buildslave", "create-slave", "--umask=022", "/app", "buildbotmaster:9989", "example-slave", "pass"]
CMD ["buildslave", "start", "--nodaemon", "/app"]

