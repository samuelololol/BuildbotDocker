#!/bin/bash
ps -ef | grep ssh-agent | grep -v grep | awk '{print $2}' | xargs kill -9
