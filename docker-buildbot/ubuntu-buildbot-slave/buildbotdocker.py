#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 18, 2015 '
__author__= 'samuel'

import os
from buildbot.plugins import *
from buildbot.status import html
from buildbot.status.web import authz, auth


GIT_REPO_URL        = os.environ['GIT_REPO_URL']
PROJECT_TITLE       = os.environ['PROJECT_TITLE']
PROJECT_URL         = os.environ['PROJECT_URL']
PROJECT_TEST_FOLDER = os.environ['PROJECT_TEST_FOLDER']

BUILDBOT_SLAVE_NAME = "example-slave"
BUILDBOT_SLAVE_PASS = "pass"
BUILDBOT_FORCE_BUILD_SCHEDULER_NAME="force"
BUILDBOT_SINGLE_BRANCH_SCHEDULER_NAME="simplify_master_cfg"
BUILDBOT_BUILDER_NAME="bugfree_builder"
BUILDSLAVE_BUILD_PATH='/app/%s/build' % BUILDBOT_BUILDER_NAME

BUILDBOT_MASTER_PROTOCOL_PORT = 9989

BUILDBOT_GITPOLLER_BRANCH = "simplify_master_cfg"
BUILDBOT_GITPOLLER_BRANCHES = None

BUILDBOT_MASTER_PORT = 8010
BUILDBOT_MASTER_AUTH_ACCOUNT = 'buildbot'
BUILDBOT_MASTER_AUTH_PASS = 'buildbot'

BUILDBOT_URL = "http://localhost:8010/"
BUILDBOT_DB_URL = "sqlite:///state.sqlite"



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


# ---------------
# factory / steps
# ---------------
BUILDBOT_FACTORY=util.BuildFactory()
BUILDBOT_FACTORY.addStep( steps.Git(repourl=GIT_REPO_URL, mode='incremental'))
BUILDBOT_FACTORY.addStep(steps.ShellCommand(
    name="check python volume",
    description="checking",
    descriptionDone="checked",
    command=["python", BUILDSLAVE_BUILD_PATH+"/"+PROJECT_TEST_FOLDER+"/check_and_create_pyvolume.py"]))

BUILDBOT_FACTORY.addStep(steps.ShellCommand(
    name="build images",
    description="building images",
    descriptionDone="built",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "build", "--no-cache"]))

BUILDBOT_FACTORY.addStep(steps.ShellCommand(
    name="test",
    description="testing",
    descriptionDone="tested",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "run", "--rm",
             "tester", "./test_runner.sh"]))

BUILDBOT_FACTORY.addStep(steps.ShellCommand(
    name="stop containers",
    description="stopping containers",
    descriptionDone="stopped",
    workdir=BUILDSLAVE_BUILD_PATH+'/'+PROJECT_TEST_FOLDER,
    command=["docker-compose", "stop"]))

BUILDBOT_FACTORY.addStep(steps.ShellCommand(
    name="remove containers",
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

