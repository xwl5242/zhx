# coding=utf-8

import json
from conf.configs import Configs
from tornado.gen import coroutine, Return
from web.base.base_handler import BaseHandler
from tornado.httpclient import AsyncHTTPClient


class FansListHandler(BaseHandler):

    config = Configs()
    openids = []

    @coroutine
    def get(self, *args, **kwargs):
        """
        获取粉丝信息入口，
        :param args:
        :param kwargs: restful风格，匹配访问地址，使用地址信息作为参数
        :return:
        """
        ret = None
        access_token = self.get_secure_cookie('access_token')
        if not access_token:
            # access_token失效,重新获取
            client = AsyncHTTPClient()
            url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential" \
                  f"&appid={self.config.APP_ID}&secret={self.config.APP_SECRET}"
            resp = yield client.fetch(url)
            ret = json.loads(resp.body)
            access_token = ret.get('access_token')
            exp = int(ret.get('expires_in'))
            self.set_secure_cookie('access_token', access_token, expires_days=exp / 60 / 60 / 24)

        if access_token:
            next = kwargs.get('next', None)
            ret = yield self.get_fans(access_token.decode(), next_openid=next)
        else:

            ret = yield self.get_fans(access_token)

        self.write(ret)

    @coroutine
    def get_fans(self, access_token, next_openid=None):
        """
        获取粉丝列表的具体实现,一次请求最多返回10000条数据(自定义为一组)和下面10000条数据的其实open_id.
        :param access_token: access_token
        :param next_openid: 下一组开始的open_id
        :return:
        """
        client = AsyncHTTPClient()
        # 获取粉丝列表请求url
        fans_url = f"https://api.weixin.qq.com/cgi-bin/user/get?" \
                   f"access_token={access_token}&next_openid={next_openid if next_openid else ''}"
        resp = yield client.fetch(fans_url)
        # 获取粉丝列表结果
        ret = json.loads(resp.body)
        if int(ret.get('count')) != 0:
            # open_id列表
            open_id_list = ret.get('data').get('openid')
            # 下一组开始的openid
            next_openid = ret.get('next_openid')
            # 存储到文件中
            with open('f://open_id.txt', 'a+') as f:
                for open_id in open_id_list:
                    f.write(f"{str(open_id)}\n")
            # 返回下一组开始的open_id
            raise Return({'next': next_openid})
        raise Return({'next', 'None'})


