# coding=utf-8

import json
from web.base.base_handler import BaseHandler
from modules.sys.dict import Dict
from modules.youtools.base_tools import BaseTools
from modules.youtools.detail_tools import DetailTools
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
        获取首页分类图标，格式[[],[],[]],list[list]
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


class ToolsIndexHandler(BaseHandler):

    def get(self):
        """
        获取首页各类型工具列表
        :return:
        """
        # 查询tools的所有种类
        tool_types = Dict.query_list("select dc_k type from sys_dic where dc_name='tools_type'")

        # 查询所有种类tools的前6名
        query_sql = "SELECT A.*, d.dc_v type_name FROM( SELECT t.* FROM t_base_tools t WHERE 3 > ( SELECT count( 1) " \
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
            # 存在tool
            if len(type_list) > 0:
                # 如果返回的list小于3个，需要考虑页面显示问题，少几个补几个空白位置
                if len(type_list) < 3:
                    for i in range(3-len(type_list)):
                        # 补空白位置
                        type_list.append({})
                tools.append({'type_name': type_name, 'tool_type': t_type, 'data': type_list})

        # 返回json数据
        self.write(json.dumps(tools))


class ToolsDetailHandler(BaseHandler):

    def get(self, *args, **kwargs):
        """
        获取工具详情
        :param args:
        :param kwargs:
        :return:
        """
        # 查询平台信息
        plat_dict = {}
        plats = Dict.query_list("select dc_k plat,dc_v plat_name from sys_dic where dc_name='plat_label'")
        for plat in plats:
            plat_dict[plat.plat] = plat.plat_name
        # 查询工具详情
        tool_id = kwargs.get('tool_id')
        tool = DetailTools.get_by_id('t_detail_tools', tool_id)
        # 处理工具的图片信息，img_urls是以分号";"为分隔的多个图片地址
        img_urls = tool.get('img_urls')
        urls = img_urls.split(';')
        # img_url 为封面图片地址
        tool['img_url'] = '' if len(urls) == 0 else urls[0]
        # img_urls 为所有该工具图片信息地址
        tool['img_urls'] = list(urls)
        # 添加tool的平台信息,windows:1;mac:2;android:3;ios:4
        tool_plat = {}
        if tool['plat_label']:
            p_ls = list(tool['plat_label'].split(','))
            for p_l in p_ls:
                tool_plat[plat_dict[p_l]] = True
            # tool['windows'] = true/false
            tool['tool_plat'] = tool_plat
        self.write(tool)


class ToolsTypeHandler(BaseHandler):

    def get(self, *args, **kwargs):
        """
        根据类型查询tool集合
        :param args:
        :param kwargs:
        :return:
        """
        # 获取请求中的tool的类型
        tool_type = kwargs.get('tool_type', '')
        # 分页信息，start：开始位置，count：显示多少个
        start = kwargs.get('start', 0)
        count = kwargs.get('count')
        # 执行查询，返回tool集合list
        tools = BaseTools.query_list(f"select t.*,d.dc_v type_name from t_base_tools t "
                                     f"left join sys_dic d on t.type = d.dc_k "
                                     f"where t.type='{tool_type}' and d.dc_name='tools_type' "
                                     f"limit {start},{start+count}")
        self.write(json.dumps(tools))


class ToolsSearchHandler(BaseHandler):

    def get(self):
        """
        根据关键字搜索
        :return:
        """
        # 获取请求中的关键字
        q = self.get_argument('q')
        # 查询sql
        query_sql = f"select t.*,d.dc_v type_name from t_base_tools t left join sys_dic d on t.type = d.dc_k " \
                    f"where d.dc_name='tools_type' and t.`name` like '%%{q}%%'"
        # 执行查询，返回tool的list
        tools = BaseTools.query_list(query_sql)
        self.write(json.dumps(tools))


