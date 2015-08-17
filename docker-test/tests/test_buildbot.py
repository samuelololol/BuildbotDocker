#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 16, 2015 '
__author__= 'samuel'

import pytest
import requests
from requests.adapters import HTTPAdapter
from BeautifulSoup import BeautifulSoup as bs
import os
import time


def test_buildbot_availible():
    #time.sleep(10)
    url = 'http://buildbotmaster:8010/json/builders/?as_text=1'
    s = requests.Session()
    s.mount(url, HTTPAdapter(max_retries=100))
    response = s.get(url)
    print 'ready to test http://buildbotmaster:8010/json/builders/?as_text=1'
    assert response.status_code == 200

