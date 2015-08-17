#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__= 'Aug 16, 2015 '
__author__= 'samuel'

import requests


import pytest
from requests.adapters import HTTPAdapter
from BeautifulSoup import BeautifulSoup as bs
import os


def test_buildbot_availible():
    url = 'http://buildbotmaster:8010/json/builders/?as_text=1'
    response = requests.get(url)
    print 'ready to test http://buildbotmaster:8010/json/builders/?as_text=1'
    assert response.status_code == 200

