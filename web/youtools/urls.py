from web.youtools.youtools_handler import *


youtools_urls = [
    (r"/banners", BannersHandler),
    (r"/icons", IconsHandler),
    (r"/tools", ToolsIndexHandler),
    (r"/tools/search", ToolsSearchHandler),
    (r"/tools/type/(?P<tool_type>[0-9a-zA-Z_-]+)/(?P<start>[0-9]+)/(?P<count>[0-9]+)", ToolsTypeHandler),
    (r"/tools/(?P<tool_id>[0-9a-zA-Z_-]+)", ToolsDetailHandler),
]

