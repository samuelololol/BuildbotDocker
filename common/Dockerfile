FROM samuelololol/ubuntu-buildbot-master
MAINTAINER samuelololol <samuelololol@gmail.com>
COPY buildbotdocker.py /app/buildbotdocker.py
ENV GIT_REPO_URL=https://github.com/samuelololol/buildbotdocker.git \
    GIT_REPO_BRANCH=master \
    PROJECT_TITLE=BuildbotDocker \
    PROJECT_URL=https://github.com/samuelololol/BuildbotDocker.git \
    PROJECT_TEST_FOLDER=test \
    TZ=Asia/Taipei \
    GIT_SSH=/usr/local/bin/git_ssh
CMD ["buildbot", "start", "--nodaemon", "/app"]

