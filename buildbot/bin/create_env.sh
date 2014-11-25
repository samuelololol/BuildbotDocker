#!/bin/bash
mkdir -p /var/lib/buildmaster/venv
virtualenv --no-site-packages /var/lib/buildmaster/venv/$1

