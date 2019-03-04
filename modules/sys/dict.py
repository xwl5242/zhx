# coding=utf-8

from modules.base.base_module import BaseModel


class Dict(BaseModel):

    def __init__(self, **kwargs):
        self.dc_name = kwargs.get('dc_name', '')
        self.dc_k = kwargs.get('dc_k', '')
        self.dc_v = kwargs.get('dc_v', '')
        self.dc_desc = kwargs.get('dc_desc', '')

