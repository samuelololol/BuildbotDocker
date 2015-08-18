FROM samuelololol/ubuntu-buildbot-base
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN ["buildbot", "create-master", "-r", "/app"]
COPY master.cfg /app/master.cfg 
COPY buildbotdocker.py /app/buildbotdocker.py
COPY git_ssh /usr/local/bin/git_ssh
ENV GIT_REPO_URL=https://github.com/samuelololol/buildbotdocker.git \
    GIT_REPO_BRANCH=master \
    PROJECT_TITLE=BuildbotDocker \
    PROJECT_URL=https://github.com/samuelololol/BuildbotDocker.git \
    PROJECT_TEST_FOLDER=test \
    TZ=Asia/Taipei \
    GIT_SSH=/usr/local/bin/git_ssh
CMD ["buildbot", "start", "--nodaemon", "/app"]

