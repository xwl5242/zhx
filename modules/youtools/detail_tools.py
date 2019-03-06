# coding=utf-8

from modules.base.base_module import BaseModel


class DetailTools(BaseModel):

    def __init__(self, **kwargs):
        self.img_url = kwargs.get('img_url', '')
        self.title = kwargs.get('title', '')
        self.comments = kwargs.get('comments', '')
        self.plat_label = kwargs.get('plat_label', '')
        self.remark = kwargs.get('remark', '')
        super(DetailTools, self).__init__(**kwargs)
