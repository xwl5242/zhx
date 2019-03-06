# coding=utf-8

from modules.base.base_module import BaseModel


class Theme(BaseModel):
    """
    主题和布局
    """
    def __init__(self, **kwargs):
        self.sidebar = kwargs.get('sidebar')
        self.navbar = kwargs.get('navbar')
        self.navbar_inverse = kwargs.get('navbar_inverse')
        self.theme_color = kwargs.get('theme_color')
        self.menu_display = kwargs.get('menu_display')
        self.menu_text_icon = kwargs.get('menu_text_icon')
        self.tab_flag = kwargs.get('tab_flag')
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