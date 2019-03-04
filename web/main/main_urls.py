from web.main.main_handler import *
from web.sys.urls import sys_urls
from web.wechat.urls import wx_urls
from web.youtools.urls import youtools_urls
from web.base.base_handler import BaseHandler

handlers = [(r"/", IndexHandler), ]

handlers.extend(youtools_urls)
handlers.extend(sys_urls)
handlers.extend(wx_urls)

handlers.extend([(r".*", BaseHandler)])

