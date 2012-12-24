# -*- coding: utf8 -*-
"""
"""
from tornado.web import RequestHandler
from gobang.libs.db import Backend

class BaseHandler(RequestHandler):
    """Handler for layout a web page
    """
    @property
    def backend(self):
        return Backend.instance()
