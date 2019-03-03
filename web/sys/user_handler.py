# coding=utf-8

from web.base.base_handler import BaseHandler
from modules.sys.user import User


class UserViewHandler(BaseHandler):
    """
    跳转到用户列表页面
    """
    def get(self):
        count = User.query_list_by_where_orderby("sys_user", is_count=True)
        return self.render_("user/list.html", user_count=count)


class UserPageHandler(BaseHandler):
    """
    用户表格查询操作，pagelist
    """
    def get(self):
        page_list = User.query_list_by_where_orderby("sys_user")
        self.write({"data": page_list})


class UserRoleHandler(BaseHandler):
    """
    查询所有的用户的角色相关信息，即所有用户信息附带各个用户所属角色的信息
    """
    def get(self):
        auth = User.query_user_role(self.get_current_user())
        self.write({"auth": auth})

