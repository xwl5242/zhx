# coding=utf-8
import tornado.web
from web.base.base_handler import BaseHandler


class IndexHandler(BaseHandler):

    @tornado.web.authenticated
    def get(self):
        self.render_("index.html")
