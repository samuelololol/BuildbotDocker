#!/bin/bash

#[[ -s "/usr/bin/virtualenvwrapper.sh"  ]] && source "/usr/bin/virtualenvwrapper.sh"
#rmvirtualenv $1 
#mkvirtualenv $1

#rm -rf /var/lib/buildmaster/venv/$1
mkdir -p /var/lib/buildmaster/venv
virtualenv --no-site-packages /var/lib/buildmaster/venv/$1

