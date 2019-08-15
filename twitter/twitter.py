# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 10:09
# @Author  : meng_zhihao
# @Email   : 312141830@qq.com
# @File    : twitter.py

from selenium_operate import ChromeOperate

import re
import time
cop = ChromeOperate(executable_path=r'chromedriver.exe',arguments=['--proxy-server=http://%s' % '127.0.0.1:1080'])

cop.open('https://twitter.com/1984to1776')


page = cop.open_source()

