#!/usr/bin/env python
# -*- coding: utf8 -*-
#服务器启动文件

import os.path
import sys

sys.path.append(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
    )
)

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define, options
from gobang.site import SiteApplication

define("port", default=7000, help="run on the given port", type=int)
define("host", default="0.0.0.0", help="run on the given host")

def run():
    options.parse_command_line()
    http_server = HTTPServer(SiteApplication())
    http_server.listen(options.port)

    print "running on %s:%d" % (options.host, options.port)
    IOLoop.instance().start()

if __name__ == "__main__":
    run()
