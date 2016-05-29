#!/usr/bin/env python
# coding:utf-8

"""
模拟登陆的基类: 实现Session相关的方法
"""

from mechanize import Browser
import cookielib


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
    LOGIN_URL = 'http://www.douban.com/accounts/login'

    # 新建一个浏览器Agent
    br = Browser()

    # 设置代理
    br.set_proxies({"http": "127.0.0.1:8888"})

    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)

    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Want debugging messages?
    # br.set_debug_http(True)
    # br.set_debug_redirects(True)
    # br.set_debug_responses(True)

    # User-Agent (this is cheating, ok?)
    br.addheaders = [('User-agent',
                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:46.0) Gecko/20100101 Firefox/46.0')]

    def __init__(self):
        self.read_config()

    # 读取配置文件
    def read_config(self):
        # TODO 后续需要做成从配置文件中获取配置
        print 'read_config' + self.__author__

    def try_login(self):
        br = self.br

        # 请求登录也
        br.open(self.LOGIN_URL)
        br.select_form(name='lzform')
        br['form_email'] = 'ziyu0123456789@gmail.com'
        br['form_password'] = ''
        resp = br.submit()
        print resp.read()

        # TODO 填写表单
