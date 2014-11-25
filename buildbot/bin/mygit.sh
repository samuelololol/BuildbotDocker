#!/bin/bash
unset SSH_ASKPASS
ssh -x -v -i /var/lib/buildmaster/bin/id_rsa -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no "$@"
