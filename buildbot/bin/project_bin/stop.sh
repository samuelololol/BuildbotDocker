#!/bin/bash
cd luwak-api
source /var/lib/buildmaster/venv/luwak/bin/activate
pserve $1 stop --pid-file=/tmp/pserved.pid
ps aux | grep pserve | awk '{print $2}' | xargs kill -9
rm -rf /tmp/pserved.pid
