#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 16, 2015 '
__author__= 'samuel'

import docker
from docker import Client
import sys
import os

CONTAINER_NAME='pytest'
IMAGE_NAME='pytest_volume'

def check_container_name(docker, cname):
    print 'check_container_name,',
    if cname in ' '.join([y.encode('utf-8').replace('/', '') for x in 
        docker.containers(all=True) for y in x['Names'] ]):
        print '"%s" container exist' % cname
        return True
    else:
        print '"%s" container not exist' % cname
        return False

def check_image_name(docker, iname):
    print 'check_image_name,',
    if iname in ' '.join([z for z in [y.encode('utf-8').split(':')[0] for x in
        docker.images() for y in x['RepoTags']] if '<none>' not in z]):
        print '"%s" image exist' % iname
        return True
    else:
        print '"%s" image not exist' % iname
        return False

def create_container(docker, name):
    print 'create_container'
    #its sharing volume described in Docker.volume file
    container = docker.create_container(image=IMAGE_NAME, name=name)
    print container


def build_image(docker, name):
    print 'build_image'
    cwd = '/'.join(os.path.abspath(__file__).split('/')[:-1])
    response = [line for line in docker.build(path=cwd+'/pytest_volume',
        tag=name, rm=True)]
    for line in response:
        print line




def main():
    global CONTAINER_NAME
    c = Client(base_url='unix://var/run/docker.sock')
    if len(sys.argv) < 2:
        name = CONTAINER_NAME
    else:
        name = sys.argv[1]

    print 'name: %s' % name

    if not check_container_name(c, name):
        if not check_image_name(c, IMAGE_NAME):
            build_image(c, IMAGE_NAME)
        create_container(c, name)
    return

if __name__ == '__main__':
    main()

