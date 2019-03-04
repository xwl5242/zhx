# coding=utf-8

from modules.base.base_module import BaseModel


class BaseTools(BaseModel):

    def __init__(self, **kwargs):
        self.type = kwargs.get('type', '')
        self.img_url = kwargs.get('img_url', '')
        self.name = kwargs.get('name', '')