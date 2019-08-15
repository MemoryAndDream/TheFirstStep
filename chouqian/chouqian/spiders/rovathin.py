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
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import scrapy
import sys,os

from chouqian.items import RovathinItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
import re

class RovathinSpider(scrapy.Spider):
    name = "rovathin"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [

    ]
    for turn_page in range(0,953,1):
        for page in range(10):
            start_urls.append('http://www.rovathin.com/products.php?turn_page=%s&page=%s'%(turn_page,page+turn_page*10))

    #def start_requests(self): #测试cookie
    #    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    #    yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies={'meng':1})

    def parse(self, response):
        base_url = get_base_url(response)
        content = response.body # 乱码处理
        segs = crawlerTool.getXpath("//table//td[2]//td/table[2]//td//table//tr//td//tr",content)
        for seg in segs[1:]:
            tds = crawlerTool.getXpath("//td", seg)
            if len(tds)<4:
                continue

            cat_no = tds[0]
            product_name = tds[1]
            cas = tds[2]
            assay = tds[3]

            rovathin_item = RovathinItem()
            rovathin_item['cat_no'] = re.sub('\s*<.*?>\s*','',cat_no)
            rovathin_item['product_name'] = re.sub('\s*<.*?>\s*','',product_name)
            rovathin_item['cas'] = re.sub('\s*<.*?>\s*','',cas)
            rovathin_item['assay'] =re.sub('\s*<.*?>\s*','',assay)
            rovathin_item['url'] =crawlerTool.getXpath1("//a/@href", product_name)
            yield rovathin_item



if __name__ == "__main__":
    from scrapy import cmdline
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl rovathin".split())


