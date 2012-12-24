# -*- coding: utf8 -*-

from gobang.libs.handlers import BaseHandler


class LoginHandler(BaseHandler):
    def get(self):
        db = self.backend
        self.render('layout/base.html');
