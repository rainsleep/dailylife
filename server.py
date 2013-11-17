#encoding:utf-8
__author__ = 'hzz'
import tornado.ioloop
import tornado.httpserver
import tornado.web
import os
from handler.handler import *
from tornado.options import define, options
# Set up current directory to program directory

define("port", default=80, help="server port", type=int)

settings = {
	"static_path":os.path.join(os.path.dirname(__file__), "static"),
    "template_path":os.path.join(os.path.dirname(__file__), "template"),
    "login_url": "/login", # 默认的登陆页面，必须有
     "cookie_secret": "__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__", # 安
}
handlers = [

	 (r"/", HomeHandler),

]
application = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
	http_server = tornado.httpserver.HTTPServer(application)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()