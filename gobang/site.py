# -*- coding: utf8 -*-
""" web app
"""
import os
import gobang as project_module

from tornado.web import Application
from gobang.apps.auth import handlers as auth_handlers
from gobang.libs.db import Backend


PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))

class SiteApplication(Application):
    def __init__(self):
        handlers = [
            (r"/login", auth_handlers.LoginHandler),
        ]
        ui_modules = {
        }
        settings = dict(
            #debug
            debug = True,

            #set modules
            ui_modules = ui_modules,

            #tornado template lookup
            template_path  = os.path.join(PROJECT_DIR, "templates"),

            #tornado httpserver static path
            static_path = os.path.join(PROJECT_DIR, "static"),

            #tmp file path
            tmp_path = os.path.join(PROJECT_DIR, "tmp"),

            #tornado auth login url
            login_url = "/login",

            #cookie settings
            xsrf_cookies = False,
            cookie_secret = 'thy_secret',

        )
        Application.__init__(self, handlers, **settings)

