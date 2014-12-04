FROM samuelololol/gentoo-buildbot:0.8
MAINTAINER samuelololol
ADD buildbot/bin /var/lib/buildmaster/bin
ADD buildbot/buildbot.tac.master /var/lib/buildmaster/buildbot.tac
ADD buildbot/buildbot.tac.slave /var/lib/buildslave/buildbot.tac
ADD buildbot/master.cfg /var/lib/buildmaster/master.cfg
RUN ["chown", "-h", "buildbot:buildbot", "/var/lib/buildmaster", "-R"]
RUN ["chown", "-h", "buildbot:buildbot", "/var/lib/buildslave", "-R"]
RUN ["emerge", "pip"]
RUN ["pip", "install", "docker-py", "pyyaml"]
