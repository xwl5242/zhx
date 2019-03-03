# coding=utf-8

from modules.base.base_module import BaseModel


class Theme(BaseModel):
    """
    主题和布局
    """
    def __init__(self, **kwargs):
        self.SIDEBAR = kwargs.get('SIDEBAR')
        self.NAVBAR = kwargs.get('NAVBAR')
        self.NAVBAR_INVERSE = kwargs.get('NAVBAR_INVERSE')
        self.THEME_COLOR = kwargs.get('THEME_COLOR')
        self.MENU_DISPLAY = kwargs.get('MENU_DISPLAY')
        self.MENU_TXT_ICON = kwargs.get('MENU_TXT_ICON')
        self.TAB_FLAG = kwargs.get('TAB_FLAG')
        super(Theme, self).__init__(**kwargs)

    # 主题表
    table = "sys_theme"

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        查询用户的主题信息
        :param user_id:
        :return:
        """
        sql = f"select {cls.get_all_columns(cls.table, join_table_alias='t')} " \
              f"from {cls.table} t left join sys_user u on t.id = u.theme_id where u.id='{user_id}'"
        theme = cls.db.get(sql)
        theme = theme if theme else cls.get_default_theme()
        return theme

    @classmethod
    def get_default_theme(cls):
        sql = f"select {cls.get_all_columns(cls.table)} from {cls.table} where id='-1'"
        return cls.db.get(sql)