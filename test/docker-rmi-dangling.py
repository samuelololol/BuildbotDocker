#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 19, 2015 '
__author__= 'samuel'

import yaml
import sys
import os
import docker
from docker import Client

def remove_images(docker):
    try:
        dangling_images_ids = \
        [id['Id'].encode('utf-8') for id in docker.images(filters={'dangling': True})]
        for id in dangling_images_ids:
            docker.remove_image(image=id, force=True, noprune=False)
            print '%s image removed' % id
    except Exception,e:
        print 'type: %s' % type(e)
        print 'args: %s' % e.args
        print str(e)

def main():
    docker = Client(base_url='unix://var/run/docker.sock')
    remove_images(docker)

if __name__ == '__main__':
    main()
