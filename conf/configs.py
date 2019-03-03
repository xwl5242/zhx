# coding=utf-8
import os
import configparser


class Configs:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(os.path.join(os.path.dirname(__file__), "config.ini"))
        self.D_MYSQL_HOST = self.get_property("Mysql-Database", "host")
        self.D_MYSQL_USER = self.get_property("Mysql-Database", "user")
        self.D_MYSQL_PASSWORD = self.get_property("Mysql-Database", "password")
        self.D_MYSQL_DATABASE = self.get_property("Mysql-Database", "database")
        self.APP_ID = self.get_property("wx", "app_id")
        self.APP_SECRET = self.get_property("wx", "app_secret")

    def get_property(self, section, option):
        return self.cf.get(section, option)

