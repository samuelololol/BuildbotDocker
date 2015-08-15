FROM samuelololol/ubuntu-buildbot-base
MAINTAINER samuelololol <samuelololol@gmail.com>
RUN ["buildbot", "create-master", "-r", "/app"]
ADD https://raw.githubusercontent.com/samuelololol/mydockerfiles/master/ubuntu-buildbot-master/master.cfg /app/master.cfg 
ENV BUILDBOT_REPO_PATH https://github.com/samuelololol/mydockerfiles.git
CMD ["buildbot", "start", "--nodaemon", "/app"]

