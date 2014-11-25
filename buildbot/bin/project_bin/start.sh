#!/bin/bash
cd luwak-api
source /var/lib/buildmaster/venv/luwak/bin/activate
pserve $1 --daemon http_port=6500 --pid-file=/tmp/pserved.pid
echo "api server pid:"
cat /tmp/pserved.pid
