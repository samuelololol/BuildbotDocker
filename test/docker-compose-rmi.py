#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 19, 2015 '
__author__= 'samuel'

import yaml
import sys
import os
import docker
from docker import Client

def check_image_name(docker, service):
    print 'check_image_name,',
    #pwd = os.path.dirname(os.path.realpath(__file__)).split('/')[-1]
    pwd = os.getcwd().split('/')[-1]
    iname = "%s_%s" % (pwd, service)
    if iname in [z for z in [y.encode('utf-8').split(':')[0] for
                       x in docker.images() for
                       y in x['RepoTags']] if '<none>' not in z]:
        print '"%s" image exist' % iname
        return (True, iname)
    else:
        print '"%s" image not exist' % iname
        return (False, None)


def remove_images(docker, composefile_name, dangling=False):
    try:
        if dangling:
            dangling_images_ids = \
            [id['Id'].encode('utf-8') for id in docker.images(filters={'dangling': True})]
            for id in dangling_images_ids:
                docker.remove_image(image=id, force=True, noprune=False)
                print '%s image removed' % id
        with open(composefile_name, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        for service in cfg:
            exist, iname = check_image_name(docker, service)
            if exist:
                docker.remove_image(image=iname, force=True, noprune=False)
                print '%s image removed' % iname
    except Exception,e:
        print 'type: %s' % type(e)
        print 'args: %s' % e.args
        print str(e)

def main():
    if len(sys.argv) == 1:
        composefile_name = 'docker-compose.yml'
    elif len(sys.argv) != 2:
        print "\n\t$ docker-compose-rmi <docekr-compose.yml>\n"
        return
    else:
        composefile_name =sys.argv[1]
    docker = Client(base_url='unix://var/run/docker.sock')
    remove_images(docker, composefile_name, dangling=True)

if __name__ == '__main__':
    main()
