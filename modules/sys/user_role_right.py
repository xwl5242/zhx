# coding=utf-8

from modules.base.base_module import BaseModel


class UserRole(BaseModel):

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id', '')
        self.role_id = kwargs.get('role_id', '')
        super(UserRole, self).__init__(**kwargs)


class RoleRight(BaseModel):

    def __init__(self, **kwargs):
        self.role_id = kwargs.get('role_id', '')
        self.right_id = kwargs.get('right_id', '')
        super(RoleRight, self).__init__(**kwargs)


