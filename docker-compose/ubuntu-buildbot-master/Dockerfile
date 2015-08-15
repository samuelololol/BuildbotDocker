FROM samuelololol/ubuntu-buildbot-base
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN ["buildbot", "create-master", "-r", "/app"]
ADD master.cfg /app/master.cfg 
ADD git_ssh /usr/local/bin/git_ssh
ENV BUILDBOT_REPO_PATH https://github.com/samuelololol/mydockerfiles.git
ENV GIT_SSH=/usr/local/bin/git_ssh
CMD ["buildbot", "start", "--nodaemon", "/app"]

