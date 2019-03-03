# coding=utf-8
import gzip
import json
from tornado.web import RequestHandler
from web.util.MenuUtil import render_child
from torndb import Row


class BaseHandler(RequestHandler):

    def prepare(self):
        """
        各个请求前的操作
        :return:
        """
        # 判断是不是pjax请求
        pjax = self.request.headers.get('X-PJAX')
        # 将要使用的模板
        self.T_N = 'PART' if pjax else 'FULL'

    def get_current_user(self):
        """
        获取当前用户
        :return: 
        """
        user_id = self.get_secure_cookie("userId")
        return user_id.decode() if user_id else None

    def get(self):
        """
        404
        :return:
        """
        self.write_error(404)

    def write_error(self, status_code, **kwargs):
        """
        错误页面跳转
        :param status_code: 状态码
        :param kwargs: 携带的信息
        :return:
        """
        if status_code == 404:
            self.render("commons/404.html")
        elif status_code == 500:
            self.render("commons/500.html")
        else:
            self.write('error:'+str(status_code))

    def render_(self, html, **kwargs):
        """
        跳转到页面的封装，携带所需的必要数据
        :param html: 页面地址
        :param kwargs: 必要数据
        :return:
        """
        user = Row(json.loads(gzip.decompress(self.get_secure_cookie("user"))))
        theme = Row(json.loads(gzip.decompress(self.get_secure_cookie("theme"))))
        right = [Row(row) for row in json.loads(gzip.decompress(self.get_secure_cookie("right")))]
        render_args = {
            'user': user,
            'theme': theme,
            'theme_json': json.dumps(theme),
            'right': right,
            'render_child': render_child,
            'T_N': self.T_N
        }
        kwargs.update(render_args)
        return self.render(html, **kwargs)

    def clear_cookies(self):
        """
        清空cookie
        :return:
        """
        self.clear_cookie("userId")
        self.clear_cookie("themeId")
        self.clear_cookie("user")
        self.clear_cookie("theme")
        self.clear_cookie("right")
