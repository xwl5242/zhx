# coding=utf-8

import json
import time
from web.base.base_handler import BaseHandler
from modules.sys.right import Right
from web.util.MenuUtil import menu_tree
from modules.sys.user_role_right import RoleRight


class RightListHandler(BaseHandler):

    def get(self):
        """
            跳转到菜单（权限）页面
        """
        self.render_('right/list.html')

    def patch(self):
        """
        查询所有权限信息
        :return:
        """
        right = Right.query_list_by_where_orderby("sys_right", where="is_del='0'", order_by=[('seq', 'asc')])
        self.write({'data': menu_tree(right, "0")})


class RightRolesHandler(BaseHandler):

    def get(self):
        """
        查询权限信息，附带该权限所属角色信息
        :return:
        """
        right_id = self.get_argument("rightId")
        self.write({'auth': Right.query_roles(right_id)})


class RightSaveHandler(BaseHandler):

    def post(self):
        """
        新增和修改曲线信息
        :return:
        """
        # 统计执行成功sql的次数
        total = 0
        # 保存或修改的菜单类型,top:顶部菜单;sub:子菜单
        menu_type = self.get_argument('type')
        # 前端传来的权限信息
        menus = json.loads(self.get_argument("menu"))
        # 需要执行操作的菜单list
        menu_list = [menus]
        if menu_type == 'sub':
            menu = self.rec_menu(menus)
            menu_list = menu
        # 当前操作的用户
        cur_user = self.get_current_user()
        # 遍历操作菜单
        for menu in menu_list:
            # 新增/修改菜单,add:新增;update:修改
            opea_type = menu['type']
            # 新增的权限所在节点的排序，查出已存在的最大权限seq值
            seq = int(Right.query_sub_max_seq(menu['pid']))
            # 初始化权限对象
            if opea_type == 'add':
                # 新增操作
                right = Right(id=menu['id'], pid=menu['pid'], right_url=menu['url'], seq=str(seq+5),
                              right_name=menu['text'], icon=menu['icon'], creator=str(cur_user), updator=str(cur_user))
                # 新增权限
                total += Right.insert('sys_right', right)
            else:
                # 修改操作
                right = Right(id=menu['id'], right_url=menu['url'], right_name=menu['text'],
                              icon=menu['icon'], update_time=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
                # 修改权限
                total += Right.update('sys_right', right, where=f" id='{menu['id']}'")
                # 删除之前的角色和权限的关系
                RoleRight.delete('sys_role_right', where=f" right_id='{menu['id']}' ")

            # 新增权限和角色关系
            auth_list = list(menu['auth'])
            for auth in auth_list:
                role_right = RoleRight(role_id=auth['id'], right_id=right['id'])
                total += RoleRight.insert('sys_role_right', role_right)
            self.write({'success': total == len(auth_list)+1})

    def rec_menu(self, menu):
        m_list = []
        child = menu.get('children', [])
        if child and len(child) > 0:
            for ch in child:
                if ch['type']:
                    m_list.append(ch)
                m_list.extend(self.rec_menu(ch))
        return m_list


class RightDeleteHandler(BaseHandler):

    def post(self, *args, **kwargs):
        """
        删除权限
        :return:
        """
        right_id = kwargs.get('id')
        if right_id:
            r_list = self.rec_right(right_id)
            r_list.append(right_id)
            for r_id in r_list:
                Right.delete('sys_right', where=f" id='{r_id}' ")
                RoleRight.delete('sys_role_right', where=f" right_id='{r_id}' ")
        self.write({'success': True})

    def rec_right(self, pid):
        right_id_list = []
        right_list = Right.query_list_by_where_orderby('sys_right', where=f" pid= '{pid}'")
        for right in right_list:
            right_id_list.append(right.get('ID'))
            right_id_list.extend(self.rec_right(right.get('ID')))
        return right_id_list


class RightUpdateTopOrder(BaseHandler):

    def post(self):
        """
        更新顶部菜单的顺序
        :return:
        """
        top_menus = json.loads(self.get_argument('topMenus'))
        total = 0
        for top_menu in top_menus:
            right_id = top_menu['id']
            seq = int(top_menu['orderNo'])
            total += Right.update_by_sql(f"update sys_right set seq={(seq-1)*5} where id='{right_id}'")
        self.write({'success': total == len(top_menus)})