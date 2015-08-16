#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 16, 2015 '
__author__= 'samuel'

import pytest
import requests
from BeautifulSoup import BeautifulSoup as bs
import os
import time


def test_buildbot_availible():
    #time.sleep(10)
    response = requests.get('http://buildbotmaster:8010/json/builders/?as_text=1')
    print 'ready to test http://buildbotmaster:8010/json/builders/?as_text=1'
    assert response.status_code == 200

