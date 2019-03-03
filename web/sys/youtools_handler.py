# coding=utf-8

import json
from web.base.base_handler import BaseHandler


class BannersHandler(BaseHandler):

    def get(self):
        """
        获取首页轮播图
        :return:
        """
        banner = [{'id': 1, 'img': '/imgs/index/banner_1.jpg', 'name': '美食', 'url': ''},
         {'id': 1, 'img': '/imgs/index/banner_2.jpg', 'name': '美食', 'url': ''},
         {'id': 1, 'img': '/imgs/index/banner_3.jpg', 'name': '美食', 'url': ''}]
        self.write(json.dumps(banner))


class IconsHandler(BaseHandler):

    def get(self):
        """
        获取首页分类图标
        :return:
        """
        icons = [[{'id': 1, 'img': '/imgs/index/icon_1.jpg', 'name': '美食', 'url': ''},
        {'id': 2, 'img': '/imgs/index/icon_2.jpg', 'name': '超市', 'url': ''},
        {'id': 3, 'img': '/imgs/index/icon_3.jpg', 'name': '鲜果购', 'url': ''},
        {'id': 4, 'img': '/imgs/index/icon_4.jpg', 'name': '下午茶', 'url': ''}]]
        self.write(json.dumps(icons))


class ToolsHandler(BaseHandler):

    def get(self):
        """
        获取首页各类型工具列表
        :return:
        """
        tools = [{'img_url': '/imgs/index/icon_1.jpg', 'name': 'google浏览器', 'shop_id': '1'},
                 {'img_url': '/imgs/index/icon_1.jpg', 'name': 'google浏览器', 'shop_id': '2'},
                 {'img_url': '/imgs/index/icon_1.jpg', 'name': 'google浏览器', 'shop_id': '3'},
                 {'img_url': '/imgs/index/icon_1.jpg', 'name': 'google浏览器', 'shop_id': '4'}]
        self.write(json.dumps(tools))
