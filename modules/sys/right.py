# coding=utf-8

from modules.base.base_module import BaseModel


class Right(BaseModel):
    """
    权限类
    """
    def __init__(self, **kwargs):
        self.PID = kwargs.get('PID', '')
        self.RIGHT_NAME = kwargs.get('RIGHT_NAME', '')
        self.RIGHT_URL = kwargs.get('RIGHT_URL', '#')
        self.RIGHT_DESC = kwargs.get('RIGHT_DESC', '')
        self.IS_LEAF = kwargs.get('IS_LEAF', '1')
        self.ICON = kwargs.get('ICON', 'wb-desktop')
        self.SEQ = kwargs.get('SEQ', '')
        super(Right, self).__init__(**kwargs)

    # 权限表名称
    table = "sys_right"

    @classmethod
    def query_by_user_id(cls, user_id):
        """
        查询指定用户的权限
        :param user_id: 用户id
        :return:
        """
        sql = f"select distinct {cls.get_all_columns(cls.table,join_table_alias='ri')} from sys_right ri " \
              f"left join sys_role_right rr on rr.right_id = ri.id " \
              f"left join sys_user_role ur on rr.role_id = ur.role_id " \
              f"left join sys_role r on rr.role_id = r.id " \
              f"where ur.user_id = {user_id} and ri.is_del = '0' order by seq"
        return cls.db.query(sql)

    @classmethod
    def query_roles(cls, right_id):
        """
        查询出角色列表，并标用permission来标出某个权限所属的角色
        :param right_id:
        :return:
        """
        # 根据right_id,判断是否需要绑定角色信息
        permission = f"group_concat((case rr.right_id when '{right_id}' then 'true' else '' end) separator '') " \
            if right_id and (right_id != str(None)) else "''"
        # 查询sql
        sql = f"select r.id,r.role_name text,{permission} permission " \
              f"from sys_role r left join sys_role_right rr on r.id=rr.role_id " \
              f"where r.is_del='0' group by r.id,r.role_name"
        return cls.db.query(sql)

    @classmethod
    def query_sub_max_seq(cls, right_id):
        """
        查询当前权限节点下子节点的最大排序数值
        :param right_id: 权限
        :return:
        """
        sql = f"select ifnull(max(seq),0) seq from sys_right where pid='{right_id}'"
        return cls.db.get(sql)['seq']
