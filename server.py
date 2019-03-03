import os
import tornado.ioloop
import tornado.web
import tornado.httpserver
from web.main.main_urls import handlers

if __name__ == '__main__':

    settings={
        "template_path": os.path.join(os.path.dirname(__file__), "templates"),
        "static_path": os.path.join(os.path.dirname(__file__), "static"),
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "login_url": "/login"
    }

    app = tornado.web.Application(
        handlers=handlers, **settings
    )
    # server = tornado.httpserver.HTTPServer(app, ssl_options={
    #     "certfile": os.path.join(os.path.abspath("."), "server.crt"),
    #     "keyfile": os.path.join(os.path.abspath("."), "server.key"),
    # })
    # server.listen(8088)
    app.listen(8088)
    tornado.ioloop.IOLoop.current().start()
