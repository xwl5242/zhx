# coding=utf-8

from modules.base.base_module import BaseModel


class Icon(BaseModel):

    def __init__(self, **kwargs):
        self.img_url = kwargs.get('img_url', '')
        self.name = kwargs.get('name', '')
        self.fragment = kwargs.get('fragment', '')
        super(Icon, self).__init__(**kwargs)
