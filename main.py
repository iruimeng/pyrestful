#!/usr/bin/env python
#-*- coding:utf-8 -*-


import router
import tornado.web
import tornado.ioloop

application = tornado.web.Application(handlers=router.routers)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
