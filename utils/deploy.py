#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = 'Dec 04, 2014'
__author__ = 'samuel'

import os
import sys
import json
from docker import Client
import yaml

import random
import string
def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

Docker_Sock_Path = '/var/www/docker.sock'

"""
command:
    create_img_on_host.py <Dockerfile> <image_name> [<docker.sock path>]

"""
def create_container(img_name, yaml_cfg, client):
    rtn_msg = {}
    section_name = yaml_cfg.keys()[0]
    #optional
    if yaml_cfg[section_name].get('ports', None):
        ports=yaml_cfg[section_name]['ports'].keys()
        port_bindings=yaml_cfg[section_name]['ports']
    else:
        ports=[]
        port_bindings={}

    #create container
    container = client.create_container(image=img_name,
                        detach=yaml_cfg[section_name]['detach'],
                        name=yaml_cfg[section_name]['name'],
                        volumes=[bs['bind'] for bs in yaml_cfg[section_name]['binds'].values()],
                        ports=ports
                        )

    rtn_msg['container_id'] = container['Id']
    rtn_msg['container_name'] = yaml_cfg[section_name]['name']

    client.start(container['Id'],
                 binds=yaml_cfg[section_name]['binds'],
                 port_bindings=port_bindings
                 )

    return rtn_msg

def create_img(dockerfile_path, img_name, client):
    if _check_duplicated_image_name(img_name, client):
        img_name = img_name.replace(':latest', '') + '_%s' % id_generator()
    with open(dockerfile_path) as f:
        response = [line for line in client.build(fileobj=f, rm=True, tag=img_name)]
    return img_name

def create_client(docker_sock_path):
    domain_socket = 'unix:/%s' % docker_sock_path
    client = Client(base_url=domain_socket)
    return client

def usage(reason):
    print reason
    print ''
    print '    $ create_img_on_host.py <Dockerfile> <image_name> [<docker.sock path>]'
    print '      (default load yaml config by `yaml` postfix to Dockerfile name)'
    sys.exit()

def main(docker_sock_path=Docker_Sock_Path):
    dockerfile_path = sys.argv[1]
    img_name =        sys.argv[2]
    client =          create_client(docker_sock_path)

    #create image
    img_name = create_img(dockerfile_path, img_name, client)
    rtn_msg = {'image_name': img_name}

    yaml_cfg =     _parse_yaml(dockerfile_path)

    #create container
    container_msg = create_container(img_name, yaml_cfg, client)
    rtn_msg.update(container_msg)
    print rtn_msg

def _check_duplicated_image_name(img_name, client):
    images = client.images()
    rtn_img = []
    for img in images:
        rtn_img += img['RepoTags']
    #debug
    #print json.dumps(rtn_img, indent=2)
    return [img for img in rtn_img if img == img_name or img == '%s:latest' % img_name]

def _parse_yaml(dockerfile_path):
    yaml_path = '%s.yaml' % dockerfile_path
    if not os.path.exists(yaml_path):
        usage('yaml file(%s) is not exists' % yaml_path)
    with open(yaml_path, 'r') as yamlfile:
        cfg = yaml.load(yamlfile)
    #check format
    if len(cfg.keys()) != 1:
        raise Exception('only 1 section is allow in yaml')

    section_name = cfg.keys()[0]
    lv_keys = ['name', 'binds', 'detach']
    binds_name = '/var/run/docker.sock'
    binds_keys = ['bind', 'ro']

    for k in lv_keys:
        if k not in cfg[section_name].keys():
            raise Exception('1st level keys error: %s disappear' % k)

    if binds_name not in cfg[section_name]['binds'].keys():
        raise Exception('binds keys error: %s != %s' % (binds_name, cfg[section_name]['binds'].keys()))

    for k in binds_keys:
        if k not in cfg[section_name]['binds'][binds_name].keys():
            raise Exception('binds keys error: %s disappear' % k)

    #debug
    print 'cfg: %s' % json.dumps(cfg, indent=2)
    return cfg


if __name__ == '__main__':
    docker_sock_path = Docker_Sock_Path

    if not os.path.exists(sys.argv[1]):
        usage('Dockerfile(%s) is not exists' % sys.argv[1])
    if not 3 <= len(sys.argv):
        usage('command arguments length < 3')
    if 3 <= len(sys.argv):
        if 3 < len(sys.argv):
            docker_sock_path = sys.argv[3]
        if not os.path.exists(docker_sock_path):
            usage('docker domain socket(%s)is not exists' % docker_sock_path)

    main(docker_sock_path)


