#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 16, 2015 '
__author__= 'samuel'

import docker
from docker import Client
import sys
import os
import json

CONTAINER_NAME='buildbotdockertestcontainer'
IMAGE_NAME='buildbotdockertest_image_volume'
VOLUME_SETTING_FOLDER=IMAGE_NAME

def recreate_volume_container(docker, cname):
    print 'recreate_volume_container,',
    if cname in ' '.join([y.encode('utf-8').replace('/', '') for x in 
        docker.containers(all=True) for y in x['Names'] ]):
        print '"%s" container exist' % cname
        remove_container(docker, cname)
    else:
        print '"%s" container not exist' % cname
    create_container(docker, cname)

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
    for line in docker.build(path=cwd+'/'+VOLUME_SETTING_FOLDER, tag=name,
                             rm=True, forcerm=True, nocache=True):
        print json.loads(line).values()[0],

def remove_container(docker, cname):
    print 'remove container: %s' % cname
    docker.remove_container(container=cname, force=True)
    print '%s removed' % cname



def main():
    global CONTAINER_NAME
    c = Client(base_url='unix://var/run/docker.sock')
    if len(sys.argv) < 2:
        name = CONTAINER_NAME
    else:
        name = sys.argv[1]

    #for remove test container's image
    if name == 'remove':
        print 'removing %s images' % IMAGE_NAME
        if IMAGE_NAME not in [y.encode('utf-8').replace('/', '') for x in c.containers(all=True) for y in x['Names']]:
            print 'image is not exist'
            return
        c.remove_image(image=IMAGE_NAME, force=True, noprune=False)
        print '%s images removed' % CONTAINER_NAME
        return

    #print 'check container name: %s' % name
    #if not recreate_volume_container(c, name):
    #    if not check_image_name(c, IMAGE_NAME):
    #        build_image(c, IMAGE_NAME)
    #    create_container(c, name)
    if not check_image_name(c, IMAGE_NAME):
        build_image(c, IMAGE_NAME)
    recreate_volume_container(c, CONTAINER_NAME)

if __name__ == '__main__':
    main()

