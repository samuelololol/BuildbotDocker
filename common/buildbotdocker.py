#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 18, 2015 '
__author__= 'samuel'

import os
from buildbot.plugins import *
from buildbot.status import html
from buildbot.status.web import authz, auth


GIT_REPO_URL        = os.environ['GIT_REPO_URL']
GIT_REPO_BRANCH     = os.environ['GIT_REPO_BRANCH']
PROJECT_TITLE       = os.environ['PROJECT_TITLE']
PROJECT_URL         = os.environ['PROJECT_URL']
PROJECT_TEST_FOLDER = os.environ['PROJECT_TEST_FOLDER']

BUILDBOT_SLAVE_NAME = "example-slave"
BUILDBOT_SLAVE_PASS = "pass"
BUILDBOT_SINGLE_BRANCH_SCHEDULER_NAME = GIT_REPO_BRANCH#"master"
BUILDBOT_FORCE_BUILD_SCHEDULER_NAME   = "force"
BUILDBOT_BUILDER_NAME = "bugfree_builder"
BUILDSLAVE_BUILD_PATH='/app/%s/build' % BUILDBOT_BUILDER_NAME

BUILDBOT_MASTER_PROTOCOL_PORT = 9989

BUILDBOT_GITPOLLER_BRANCH = GIT_REPO_BRANCH #"master" #from os.environ
BUILDBOT_GITPOLLER_BRANCHES = None
BUILDBOT_GIT_POLLINTERVAL = 300

BUILDBOT_MASTER_PORT = 8010
BUILDBOT_MASTER_AUTH_ACCOUNT = 'buildbot'
BUILDBOT_MASTER_AUTH_PASS = 'buildbot'

BUILDBOT_URL = "http://localhost:8010/"
BUILDBOT_DB_URL = "sqlite:///state.sqlite"

_PROJECT_TESTER_SERVICE_NAME = "buildbottester999test"
_TO_DELETE_IMAGES = "%s_%s" % (PROJECT_TEST_FOLDER, service) for service in 
                                           ["buildbotmaster999test",
                                            "buildbotslave999test",
                                            "buildbottester999test"]



# ----------
# schedulers
# ----------
BUILDBOT_SCHEDULERS = [
        schedulers.SingleBranchScheduler(
            name=BUILDBOT_SINGLE_BRANCH_SCHEDULER_NAME,
            change_filter=util.ChangeFilter(branch=BUILDBOT_GITPOLLER_BRANCH),
            treeStableTimer=None,
            builderNames=[BUILDBOT_BUILDER_NAME]),
        schedulers.ForceScheduler(
            name=BUILDBOT_FORCE_BUILD_SCHEDULER_NAME,
            builderNames=[BUILDBOT_BUILDER_NAME])
        ]


# -------------
# factory/steps
# -------------
BUILDBOT_FACTORY_FOR_TEST=util.BuildFactory()
BUILDBOT_FACTORY_FOR_TEST.addStep( steps.Git(repourl=GIT_REPO_URL, mode='incremental'))
BUILDBOT_FACTORY_FOR_TEST.addStep(steps.ShellCommand(
    name="check python volume",
    description="checking",
    descriptionDone="checked",
    command=["python", BUILDSLAVE_BUILD_PATH+"/"+PROJECT_TEST_FOLDER+"/check_and_create_pyvolume.py"]))

BUILDBOT_FACTORY_FOR_TEST.addStep(steps.ShellCommand(
    name="build images",
    description="building images",
    descriptionDone="built",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "build", "--no-cache"]))

BUILDBOT_FACTORY_FOR_TEST.addStep(steps.ShellCommand(
    name="test",
    description="testing",
    descriptionDone="tested",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "run", "--rm",
             _PROJECT_TESTER_SERVICE_NAME, "./test_runner.sh"]))

BUILDBOT_FACTORY_FOR_TEST.addStep(steps.ShellCommand(
    name="stop containers",
    description="stopping containers",
    descriptionDone="stopped",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "stop"]))

BUILDBOT_FACTORY_FOR_TEST.addStep(steps.ShellCommand(
    name="remove containers",
    description="removing containers",
    descriptionDone="removed",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "rm", "-f"]))

BUILDBOT_FACTORY_FOR_TEST.addStep(steps.ShellCommand(
    name="remove tester image",
    description="removing containers",
    descriptionDone="removed",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "rm", "-f"]))

# ------
# status
# ------
BUILDBOT_MASTER_AUTHZ_CFG=authz.Authz(
    # change any of these to True to enable; see the manual for more
    # options
    auth=auth.BasicAuth([(BUILDBOT_MASTER_AUTH_ACCOUNT, BUILDBOT_MASTER_AUTH_PASS)]),
    gracefulShutdown = False,
    forceBuild = 'auth', # use this to test your slave once it is set up
    forceAllBuilds = 'auth',  # ..or this
    pingBuilder = False,
    stopBuild = False,
    stopAllBuilds = False,
    cancelPendingBuild = False,
)

