#!/bin/bash
#
# date: 2014/12/05
# author: samuel

mkdir -p /var/lib/buildmaster/venv
virtualenv --no-site-packages /var/lib/buildmaster/venv/$1

