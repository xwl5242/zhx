# coding=utf-8
from modules.base.base_module import BaseModel


class Role(BaseModel):
    """
    用户
    """
    def __init__(self, **kwargs):
        self.ROLE_NAME = kwargs.get('ROLE_NAME', '')
        self.ROLE_DESC = kwargs.get('ROLE_DESC', '')
        super(Role, self).__init__(**kwargs)

    # 角色表
    table = "sys_role"

    @classmethod
    def query_usercounts(cls):
        """
        查询角色，附带各个角色所拥有的用户个数
        :return:
        """
        sql = "select A.id,A.role_name,count(A.user_id) total " \
              "from (select r.id,r.role_name,ur.user_id from sys_role r " \
              "left join sys_user_role ur on r.id=ur.role_id where r.is_del='0')A group by A.id,A.role_name"
        return cls.db.query(sql)

    @classmethod
    def query_user(cls, role_id):
        """
        根据角色id查询用户信息
        :param role_id:
        :return:
        """
        where = f' and ur.role_id = {role_id} ' if role_id else ''
        sql = f"select distinct {cls.get_all_columns(table='sys_user',join_table_alias='u')} " \
              f"from sys_user u left join sys_user_role ur on u.id = ur.user_id where 1=1 {where}"
        return cls.db.query(sql)

    @classmethod
    def query_rights(cls, role_id):
        """
        查询角色相关的权限信息，
        如果role_id为空，则不查询STATE字段，STATE字段主要用来标注该角色是否拥有此权限
        :param role_id:
        :return:
        """
        sql = ''
        if role_id:
            sql = f"SELECT r.id ID, r.pid PID, r.right_name RIGHT_NAME, r.right_url RIGHT_URL, r.icon ICON, " \
                  f"group_concat((CASE rr.role_id WHEN  '{role_id}' THEN 'true' ELSE '' END ) separator '') STATE " \
                  f"FROM sys_right r LEFT JOIN sys_role_right rr ON r.id = rr.right_id WHERE r.is_del = '0' " \
                  f"group by r.id, r.right_name, r.right_url, r.icon"
        else:
            sql = f"SELECT r.id ID, r.pid PID, r.right_name RIGHT_NAME, r.right_url RIGHT_URL, r.icon ICON, '' STATE " \
                  f"FROM sys_right r LEFT JOIN sys_role_right rr ON r.id = rr.right_id WHERE r.is_del = '0' " \
                  f"group by r.id, r.right_name, r.right_url, r.icon"
        return cls.db.query(sql)

