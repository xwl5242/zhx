# coding=utf-8

from modules.base.base_module import BaseModel


class Banner(BaseModel):

    def __init__(self, **kwargs):
        self.img_url = kwargs.get('img_url', '')
        self.name = kwargs.get('name', '')
        self.url = kwargs.get('url', '')