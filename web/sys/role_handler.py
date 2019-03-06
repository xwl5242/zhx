# coding=utf-8

import json
from web.base.base_handler import BaseHandler
from modules.sys.role import Role
from modules.sys.user_role_right import RoleRight, UserRole
from web.util.MenuUtil import right_tree


class RoleUserCountHandler(BaseHandler):
    """
    查询角色信息，附带该角色下的用户个数
    """
    def get(self):
        self.write({'role': Role.query_usercounts()})


class RoleUserHandler(BaseHandler):
    """
    根据角色id查询用户
    """
    def get(self):
        role_id = self.get_argument("roleId")
        self.write({'data': Role.query_user(role_id)})


class RoleRightTreeHandler(BaseHandler):
    """
    查询角色的权限信息
    """
    def get(self):
        role_id = self.get_argument("roleId")
        rights = right_tree(Role.query_rights(role_id), '0')
        self.write(json.dumps(rights))


class RoleSaveHandler(BaseHandler):
    """
    新增或修改角色信息
    """
    def post(self):
        # 操作成功的条数
        deal_total = 0
        # 获取请求参数
        role_id = self.get_argument("roleId")
        role_name = self.get_argument("roleName")
        role_auth = self.get_argument("roleAuth")
        if role_id:
            # 修改
            role = Role(id=role_id, role_name=role_name, role_desc=role_name)
            deal_total += Role.update('sys_role', role, where=f" id='{role_id}' ")
            # 需要删除之前的角色和权限的关系
            RoleRight.delete('sys_role_right', where=f" role_id='{role_id}'")
        else:
            # 新增
            role = Role(role_name=role_name, role_desc=role_name)
            deal_total += Role.insert('sys_role', role)
        # 新增角色和权限的关系
        for right_id in role_auth.split(','):
            role_right = RoleRight(role_id=role['id'], right_id=right_id)
            deal_total += RoleRight.insert('sys_role_right', role_right)
        # 返回页面,id是用来刷新页面使用的
        self.write({'success': deal_total == len(role_auth.split(','))+1, 'id': role['id']})


class RoleDeleteHandler(BaseHandler):
    """
    删除角色信息
    """
    def post(self, *args, **kwargs):
        total = 0
        role_id = kwargs.get('roleId')
        role_id = role_id.split(',')
        for id in role_id:
            # 删除角色信息
            total = Role.delete('sys_role', where=f" id='{id}'")
            # 删除角色相关联的权限信息
            RoleRight.delete('sys_role_right', where=f" role_id='{id}'")
            # 删除角色相关联的用户信息
            UserRole.delete('sys_user_role', where=f" role_id='{id}'")
        self.write({'success': total == 1})
