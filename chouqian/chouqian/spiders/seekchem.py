# -*- coding: utf-8 -*-
"""
File Name：     seekchem
Description :
Author :       meng_zhihao
mail :       312141830@qq.com
date：          2019/6/13
"""

if __name__ == "__main__":
    from scrapy import cmdline
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import scrapy
import sys,os

from chouqian.items import SeekchemItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
import re
from urlparse import urljoin

class SeekchemSpider(scrapy.Spider):
    name = "seekchem"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [

    ]
    for page in range(1,10,1):
       start_urls.append('http://www.seekchem.com/cas_%s/'%(page))

    #def start_requests(self): #测试cookie
    #    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    #    yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies={'meng':1})

    def parse(self, response):
        base_url = get_base_url(response)
        url_now = response.url
        response_content = response.body  # 乱码处理
        segs = crawlerTool.getXpath('//div[@class="cas_default_list_star "]//ul', response_content)
        for seg in segs[1:-1]:
            data_obj = SeekchemItem()
            lis=crawlerTool.getXpath('//li',seg)
            data_obj['url'] = crawlerTool.getXpath1('//a/@href',lis[0])
            data_obj['cas'] =  crawlerTool.getXpath1('//b/text()',lis[0])
            data_obj['name'] = crawlerTool.getXpath1('//text()',lis[1])
            yield data_obj

        # next_page = crawlerTool.getXpath1("//a[@class='next']/@href", response_content)
        # next_page_url = urljoin(url_now,next_page)
        # yield scrapy.Request(url=next_page_url, callback=self.parse)
        page_urls = crawlerTool.getXpath( '//div[@class="pages"]/a/@href', response_content)
        for page_url in page_urls:
            yield scrapy.Request(urljoin(url_now,page_url), callback=self.parse)



if __name__ == "__main__":
    from scrapy import cmdline
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl seekchem".split())


