#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.web

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

#替代数据库或者缓存
secretMap = {'my_key' : 'wer123'}

class CreateToken(tornado.web.RequestHandler):
    '''
    获取token控制器
    '''

    STATUS_OK = 0
    STATUS_NO = 1

    def post(self):
        key = self.get_argument("api_key", 'my_key')
        #secret_key = self.get_argument("secret_key", '')

        if key == '' or key not in secretMap:
            response = {'errno' : self.STATUS_NO, 'msg': 'api_key is illegal'}
            self.write(response)
            return

        #10分钟key过期
        s = Serializer(secretMap.get(key), 600)
        token = s.dumps({'secret_key':secretMap.get(key)})

        response = {'errno' : self.STATUS_OK, 'token' :  token}
        self.write(response)



class VerifyToken(object):
    """
    验证token是否合法
    """
    def __init__(self, apiKey, token):
        self.key = apiKey 
        self.token = token

    def verify(self):
        if self.token == '' or self.key == '':
            return None

        s = Serializer(secretMap.get(self.key))
        try:
            data = s.loads(self.token)
        except:
            return None

        return data.get('secret_key') == secretMap.get(self.key)


