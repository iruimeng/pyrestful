#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#from model import createTocken
from model import *

routers = [
    (r'/', index.IndexHandler),
    (r'/createToken', token.CreateToken),
]


