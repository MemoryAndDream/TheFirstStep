# -*- coding: utf-8 -*-
"""
File Name：     angenechemical
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2019/3/19
"""
# -*- coding: utf-8 -*-
# encoding: utf-8

"""
@author: Meng.ZhiHao
@contact: 312141830@qq.com
@file: cou_qian_spider.py
@time: 2018/1/10 13:45
"""
if __name__ == "__main__":
    from scrapy import cmdline
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import scrapy

from chouqian.items import angenechemical_item
import json
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser


class Angenechemical(scrapy.Spider):
    name = "angenechemical"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [
    ]
#    数据总量23000条

    def start_requests(self): #测试cookie
        for i in range(107100,131947,1):
            #https://www.caymanchem.com/Search?q=*%3A*&fq=raptas%3ARAP000258
            url = 'http://www.angenechemical.com/caslist.html?page=%s'%i
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        base_url = get_base_url(response)
        response_content = response.body # 乱码处理 #像https://www.chemicalbook.com/ShowSupplierProductsList6187/51100.htm有9万多
        # cat_name = response.meta.get('cat_name')
        segs = crawlerTool.getXpath('//li[@class="list-group-item"]/text()', response_content)
        for seg in segs:
            data_obj = angenechemical_item()
            data_obj['url'] = seg
            yield data_obj




if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl angenechemical".split())


