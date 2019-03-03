from web.wechat.wx import *

wx_urls = [
    (r"/fans", FansListHandler),
    (r"/fans/(?P<next>[a-zA-Z0-9_-]+)", FansListHandler),
]