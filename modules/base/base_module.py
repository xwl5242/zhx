# coding=utf-8

import uuid
import time
import torndb
from conf.configs import Configs


class BaseModel(dict):

    """
        基础module类,实现了基本的数据库操作(增删改查)
    """
    # configs: 项目配置文件, 位置conf / config.ini
    configs = Configs()

    # db: 数据库连接
    db = torndb.Connection(
        host=configs.D_MYSQL_HOST,
        database=configs.D_MYSQL_DATABASE,
        user=configs.D_MYSQL_USER,
        password=configs.D_MYSQL_PASSWORD
    )

    def __init__(self, **kwargs):
        self.id = kwargs.get('id') if kwargs.get('id') else ''.join(str(uuid.uuid4()).split('-'))
        self.is_del = kwargs.get('is_del', '0')
        self.creator = kwargs.get('creator', '')
        self.create_time = kwargs.get('create_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.updator = kwargs.get('updator', '')
        self.update_time = kwargs.get('update_time', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        return self[item]

    def __str__(self):
        kvs = []
        for item in self.items():
            kvs.append(f"'{item[0]}':'{item[1]}'")
        return '{'+','.join(kvs)+'}'

    @classmethod
    def get_all_columns(cls, table, join_table_alias=None):
        """
        根据表名称获取该表的所有字段str:(ID,NAME),如提供外连接表名称则str:(t.ID,t.name)
        :param table: 表名称
        :param join_table_alias: 存在外链接时主表的表名称,主要是针对存在多表查询,并且查询结果只要主表的字段时
        :return: 该表所有字段字符串:ID,NAME...
        """
        if join_table_alias:
            # 提供主表别名时
            sql = f"select group_concat(concat('{join_table_alias}','.',column_name)) cns " \
                  f"from information_schema.columns " \
                  f"where table_name='{table}' and TABLE_SCHEMA='{cls.configs.D_MYSQL_DATABASE}'"
        else:
            sql = f"select group_concat(column_name) cns from information_schema.columns " \
                  f"where table_name='{table}' and TABLE_SCHEMA='{cls.configs.D_MYSQL_DATABASE}'"
        # 返回字段字符串
        columns_str = cls.db.get(sql)['cns']
        return columns_str.lower()

    @classmethod
    def insert(cls, table, model):
        """
        新增操作
        :param table: 表名称
        :param model: 需要插入的表对象,需要注意的是model的各个字段名称要和数据库表中的列名称相对应
        :return: 成功插入的记录数
        """
        # 获取字段值
        values = []
        columns = cls.get_all_columns(table).split(',')
        for column in columns:
            values.append(f"'{model[column]}'")
        # 拼接新增sql
        sql = f"insert into {table} ({cls.get_all_columns(table)}) " \
              f"values ({','.join([str(value) for value in values])})"
        # 执行新增操作
        return cls.db.execute_rowcount(sql)

    @classmethod
    def insert_by_sql(cls, sql):
        """
        根据sql新增
        :param sql: 新增sql
        :return:
        """
        return cls.db.execute_rowcount(sql)

    @classmethod
    def update(cls, table, model, where=None):
        """
        更新操作
        :param table: 表名称
        :param model: 需要更新的表对象
        :param where: 更新条件
        :return:
        """
        sets = []
        for k, v in model.items():
            if v:
                sets.append(f" {k}='{v}' ")
        sql = f"update {table} set {','.join(sets)} where {where if where else '1=1'}"
        return cls.db.execute_rowcount(sql)

    @classmethod
    def update_by_sql(cls, sql):
        """
        根据sql更新
        :param sql: 更新sql
        :return:
        """
        return cls.db.execute_rowcount(sql)

    @classmethod
    def delete(cls, table, where=None):
        """
        删除数据
        :param table: 表名称
        :param where: 删除条件
        :return:
        """
        return cls.update(table, {'is_del': '1'}, where=where)

    @classmethod
    def delete_by_sql(cls, sql):
        """
        删除数据
        :param sql: 删除语句
        :return:
        """
        return cls.db.execute_rowcount(sql)

    @classmethod
    def get_by_id(cls, table, primary_key):
        """
        主键查询，获取单条数据
        :param table: 表名称
        :param primary_key: 主键
        :return: 记录
        """
        columns = cls.get_all_columns(table)
        sql = f"select {columns} from {table} where id={primary_key}"
        return cls.db.get(sql)

    @classmethod
    def query_list(cls, sql):
        """
        查询list
        :param sql: 查询语句
        :return: list
        """
        return cls.db.query(sql)

    @classmethod
    def query_list_by_where_orderby(cls, table, order_by=None, where=None, is_count=False):
        """
        查询list
        :param table: 表名称
        :param order_by: 排序条件
        :param where: where条件
        :param is_count: 是否查询记录条数
        :return: list
        """
        assert type(is_count) == bool, 'is_count:布尔类型,True/False'

        # 处理排序字符串
        order_by_str = ''
        try:
            if order_by:
                order_by_str = ' order by '
                for x, y in order_by:
                    order_by_str += f' {x} {y},'
        except AttributeError:
            raise Exception('order_by pattern is [(column_name,asc/desc),(column_name,asc/desc),...]:'
                            'order_by参数的格式为 列表[元组(列名称,升序/降序),元组()...]')

        # 得到排序str
        order_by_str = order_by_str[:len(order_by_str)-1]
        # 表中所有的列名称
        columns = cls.get_all_columns(table)
        # 查询语句
        sql = f"select {columns if not is_count else 'count(1) total'} " \
              f"from {table} where {where if where else ' 1=1 '} {order_by_str}"
        result = cls.query_list(sql)
        return result[0].get('total') if is_count else result
