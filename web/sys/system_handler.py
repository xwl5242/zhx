# coding=utf-8

from web.base.base_handler import BaseHandler


class SystemLockHandler(BaseHandler):
    """
    锁屏操作
    """
    def get(self):
        # 清空cookie信息
        self.clear_cookies()
        self.render_('system/locked.html')


class SystemSettingsHandler(BaseHandler):
    """
    设置主题与布局
    """
    def get(self):
        self.render_('system/settings/display.html')
