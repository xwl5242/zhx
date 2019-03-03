# coding = utf-8

from web.sys.login_handler import *
from web.sys.user_handler import *
from web.sys.role_handler import *
from web.sys.right_handler import *
from web.sys.system_handler import *
from web.sys.youtools_handler import *

sys_urls = [
    (r"/banners", BannersHandler),
    (r"/icons", IconsHandler),
    (r"/tools", ToolsHandler),
    (r"/home", HomeHandler),
    (r"/captcha", CaptchaHandler),
    (r"/login", LoginHandler),
    (r"/logout", LogoutHandler),
    (r"/user/list", UserViewHandler),
    (r"/user/pagelist", UserPageHandler),
    (r"/user/role", UserRoleHandler),
    (r"/role/usercounts", RoleUserCountHandler),
    (r"/role/user", RoleUserHandler),
    (r"/role/rights", RoleRightTreeHandler),
    (r"/role/save", RoleSaveHandler),
    (r"/role/delete/(?P<roleId>[0-9a-zA-Z_-]+)", RoleDeleteHandler),
    (r"/right/list", RightListHandler),
    (r"/right/roles", RightRolesHandler),
    (r"/right/save", RightSaveHandler),
    (r"/right/delete/(?P<id>[0-9a-zA-z_-]+)", RightDeleteHandler),
    (r"/right/update_top_order", RightUpdateTopOrder),
    (r"/system/locked", SystemLockHandler),
    (r"/system/settings", SystemSettingsHandler),
]