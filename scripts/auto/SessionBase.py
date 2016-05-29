#!/usr/bin/env python
# coding:utf-8

"""
模拟登陆的基类: 实现Session相关的方法
"""

from mechanize import Browser


class SessionBase:

    # 版本信息说明
    __author__ = 'aiziyuer'
    __version__ = "1.0.1"
    __date__ = '2016.5.29'
    __copyright__ = 'Copyright 2016, aiziyuer.com'
    __license__ = 'GPL'
    __credits__ = ['aiziyuer']
    __maintainer__ = 'aiziyuer'
    __email__ = 'ziyu0123456789@gmail.com'
    __status__ = 'Developing'

    # 登录的URL TODO 后面需要做到配置文件里面去
    LOGIN_URL = 'http://www.douban.com'
    # 新建一个浏览器Agent
    br = Browser()

    def __init__(self):
        self.read_config()

    # 读取配置文件
    def read_config(self):
        # TODO 后续需要做成从配置文件中获取配置
        print 'read_config' + self.__author__

    def try_login(self):
        # 请求登录也
        self.br.follow_link(self.LOGIN_URL)

        # TODO 填写表单
