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

from chouqian.items import ChemicalBook
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
class ChemicalSpider(scrapy.Spider):
    name = "chemicalbook"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [
        "https://www.chemicalbook.com/ProductSupplierlist_%s_200.htm"%str(i) for i in range(36,61,1) # (36,61,1)
        # 36 37 已做
    ]

    #def start_requests(self): #测试cookie
    #    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    #    yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies={'meng':1})

    def parse(self, response):
        base_url = get_base_url(response)
        response_content = response.body # 乱码处理 #像https://www.chemicalbook.com/ShowSupplierProductsList6187/51100.htm有9万多
        suburls = crawlerTool.getXpath("//table[@id='ContentPlaceHolder1_ProductClassDetail']//tr/td[1]/a/@href",response_content)
        for suburl in suburls:
            suburl = urljoin(base_url,suburl)
            yield scrapy.Request(url=suburl,callback = self.parser_sub)
        next_page_url = crawlerTool.getXpath('//div[@align="center"]/a/@href',response_content)
        if next_page_url:
            for page_url in next_page_url:  # 重试
                page_url = urljoin(base_url,page_url)
                yield scrapy.Request(url=page_url, callback=self.parse)


    def parser_sub(self,response):
        base_url = get_base_url(response)
        response_content = response.body # 乱码处理
        url= response.url
        #detail =crawlerTool.getXpath('//div[@id="ContentPlaceHolder1_SupplierContact"]',response_content)[0] # 关于我们
       # response_content = unicode(response_content, 'gbk') # http://www.hxchem.net/companydetaildesenborn.html 这个就不行了！
        # lxwm = HTMLParser().unescape(lxwm)
        # lxwm=lxwm.encode('utf8')
        data_obj = ChemicalBook()
        data_obj['url'] = url
        data_obj['name'] = crawlerTool.getXpath('//div[@id="ContentPlaceHolder1_SupplierContact"]/table[2]//tr[2]/td[2]/a/text()',response_content)[0]
        data_obj['lxdh'] = crawlerTool.getXpath1('//div[@id="ContentPlaceHolder1_SupplierContact"]/table[2]//tr[3]/td[2]//text()',response_content)
        data_obj['email'] = crawlerTool.getXpath1('//div[@id="ContentPlaceHolder1_SupplierContact"]/table[2]//tr[5]/td[2]//text()',response_content)
        data_obj['wz'] = crawlerTool.getXpath1('//div[@id="ContentPlaceHolder1_SupplierContact"]/table[2]//tr[6]/td[2]//text()',response_content)
        cplb_div = crawlerTool.getXpath('//div[@id="ContentPlaceHolder1_ProductSupplier"]//table',response_content)[3:-1]
        print data_obj['name'].encode('unicode-escape').decode('string_escape')
        cplb = []
        for cp in cplb_div:
            chinese_name = crawlerTool.getXpath('//tr/td[2]/text()',cp)
            chinese_name = chinese_name[0] if chinese_name else ''
            cps = crawlerTool.getXpath('//tr/td[3]/text()', cp)
            cps = cps[0] if cps else ''
            cplb.append(' '.join([chinese_name,cps]))
        data_obj['cplb'] = cplb
       # print lxr,dz,yb,dh,sj
        yield data_obj
        page_urls = crawlerTool.getXpath('//div[@id="ContentPlaceHolder1_ProductSupplier"]//table[2]//tr[2]/td[2]//a/@href',response_content)
        for page_url in page_urls:
            page_url = urljoin(base_url,page_url)
            yield scrapy.Request(url=page_url, callback=self.parser_sub)




if __name__ == "__main__":
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl chemicalbook".split())


