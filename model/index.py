#!/usr/bin/env python
#-*- coding:utf-8 -*-

import token
import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    '''
    demo
    '''
    def get(self):
        #self.write("hello world")
        key = self.get_argument('api_key')
        ken = self.get_argument('token')
        Obj = token.VerifyToken(key, ken)

        if Obj.verify():
            self.write('ok')
        else:
            self.write('error')

