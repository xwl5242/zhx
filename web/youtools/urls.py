from web.youtools.youtools_handler import *


youtools_urls = [
    (r"/banners", BannersHandler),
    (r"/icons", IconsHandler),
    (r"/tools", ToolsHandler),
    (r"/tools/(?P<tool_id>[0-9a-zA-Z_-]+)", DetailToolsHandler)
]

