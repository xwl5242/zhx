# coding=utf-8

import json
from web.base.base_handler import BaseHandler
from modules.sys.dict import Dict
from modules.youtools.base_tools import BaseTools
from modules.youtools.banner import Banner
from modules.youtools.icon import Icon


class BannersHandler(BaseHandler):

    def get(self):
        """
        获取首页轮播图
        :return:
        """
        banner = Banner.query_list("select * from t_banner where is_del='0' ORDER BY seq asc")
        self.write(json.dumps(banner))


class IconsHandler(BaseHandler):

    def get(self):
        """
        获取首页分类图标
        :return:
        """
        icons_list = Icon.query_list("select * from t_icon where is_del='0' ORDER BY seq asc")
        i = 1
        icons = []
        icon_list = []
        for icon in icons_list:
            if i % 4 == 0:
                icon_list.append(icon)
                icons.append(icon_list)
                icon_list = []
            else:
                icon_list.append(icon)
            i += 1
        icons.append(icon_list)
        self.write(json.dumps(icons))


class ToolsHandler(BaseHandler):

    def get(self):
        """
        获取首页各类型工具列表
        :return:
        """
        # 查询tools的所有种类
        tool_types = Dict.query_list("select dc_k type from sys_dic where dc_name='tools_type'")

        # 查询所有种类tools的前6名
        query_sql = "SELECT A.*, d.dc_v type_name FROM( SELECT t.* FROM t_base_tools t WHERE 6 > ( SELECT count( 1) " \
                    "FROM t_base_tools WHERE type = t.type AND seq < t.seq AND is_del = '0' ) ) A " \
                    "LEFT JOIN sys_dic d ON A.type = d.dc_k WHERE d.dc_name = 'tools_type' ORDER BY A.type, A.seq ASC"
        tool_list = BaseTools.query_list(query_sql)
        # 处理tool_list数据
        tools = []
        for tool_type in tool_types:
            type_list = []
            type_name = ''
            t_type = ''
            for tool in tool_list:
                if tool['type'] == tool_type['type']:
                    type_name = tool['type_name']
                    t_type = tool['type']
                    type_list.append(tool)
            if len(type_list)>0:
                tools.append({'type_name': type_name, 'tool_type': t_type, 'data': type_list})
        # 返回json数据
        self.write(json.dumps(tools))
