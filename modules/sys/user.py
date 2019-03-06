# coding=utf-8
from modules.base.base_module import BaseModel


class User(BaseModel):
    """
    用户
    """
    def __init__(self, **kwargs):
        self.user_code = kwargs.get('user_code', '')
        self.user_name = kwargs.get('user_name', '')
        self.password = kwargs.get('password', '')
        self.nick_name = kwargs.get('nick_name', '')
        self.phone = kwargs.get('phone', '')
        self.mail = kwargs.get('mail', '')
        self.sex = kwargs.get('sex', '')
        self.age = kwargs.get('age', '')
        self.type = kwargs.get('type', '')
        self.use_status = kwargs.get('use_status', '')
        self.last_login_time = kwargs.get('last_login_time', '')
        self.login_total = kwargs.get('login_total', '')
        self.theme_id = kwargs.get('theme_id', '')
        super(User, self).__init__(**kwargs)

    # 用户表
    table = "sys_user"

    @classmethod
    def get_by_code(cls, code):
        """
        根据用户编号(user_code)获取用户
        :param code: 用户编号  user_code
        :return:
        """
        sql = f"select {cls.get_all_columns(cls.table)} from {cls.table} where user_code='{code}'"
        return cls.db.get(sql)

    @classmethod
    def query_user_role(cls, user_id):
        """
        查询用户信息，附带用户所附的角色
        :param user_id:
        :return:
        """
        sql = f"select r.id, r.role_name text," \
              f"group_concat((case ur.user_id when '{user_id}' then 'true' else '' end) separator '') permission " \
              f"from sys_role r LEFT JOIN sys_user_role ur on r.id = ur.role_id group by r.id,r.role_name"
        return cls.db.query(sql)
