# coding=utf-8
from modules.base.base_module import BaseModel


class User(BaseModel):
    """
    用户
    """
    def __init__(self, **kwargs):
        self.USER_CODE = kwargs.get('USER_CODE', '')
        self.USER_NAME = kwargs.get('USER_CODE', '')
        self.PASSWORD = kwargs.get('USER_CODE', '')
        self.NICK_NAME = kwargs.get('USER_CODE', '')
        self.PHONE = kwargs.get('USER_CODE', '')
        self.MAIL = kwargs.get('USER_CODE', '')
        self.SEX = kwargs.get('USER_CODE', '')
        self.AGE = kwargs.get('USER_CODE', '')
        self.TYPE = kwargs.get('USER_CODE', '')
        self.USE_STATUS = kwargs.get('USER_CODE', '')
        self.LAST_LOGIN_TIME = kwargs.get('USER_CODE', '')
        self.LOGIN_TOTAL = kwargs.get('USER_CODE', '')
        self.THEME_ID = kwargs.get('USER_CODE', '')
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
