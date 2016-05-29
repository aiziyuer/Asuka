#!/usr/bin/env python
# coding:utf-8

"""
模拟登陆的基类: 实现Session相关的方法
"""


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

    def __init__(self):
        print 'hello'

    # 读取配置文件
    def read_config(self):
        print 'read_config' + self.__author__

    def try_login(self):
        print 'hello world' + self.__author__
