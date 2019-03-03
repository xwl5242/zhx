# coding=utf-8

from modules.base.base_module import BaseModel


class UserRole(BaseModel):

    def __init__(self, **kwargs):
        self.USER_ID = kwargs.get('USER_ID', '')
        self.ROLE_ID = kwargs.get('ROLE_ID', '')
        super(UserRole, self).__init__(**kwargs)


class RoleRight(BaseModel):

    def __init__(self, **kwargs):
        self.ROLE_ID = kwargs.get('ROLE_ID', '')
        self.RIGHT_ID = kwargs.get('RIGHT_ID', '')
        super(RoleRight, self).__init__(**kwargs)


