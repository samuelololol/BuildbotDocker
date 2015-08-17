FROM samuelololol/ubuntu-buildbot-base
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN ["buildbot", "create-master", "-r", "/app"]
ADD master.cfg /app/master.cfg 
ADD buildbotdocker.py /app/buildbotdocker.py
ADD git_ssh /usr/local/bin/git_ssh
ENV GIT_REPO_URL=https://github.com/samuelololol/buildbotdocker.git PROJECT_TITLE=BuildbotDocker PROJECT_URL=https://github.com/samuelololol/BuildbotDocker.git TZ=Asia/Taipei GIT_SSH=/usr/local/bin/git_ssh
CMD ["buildbot", "start", "--nodaemon", "/app"]

