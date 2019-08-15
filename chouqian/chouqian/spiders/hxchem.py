# encoding: utf-8  

""" 
@author: Meng.ZhiHao 
@contact: 312141830@qq.com 
@file: cou_qian_spider.py 
@time: 2018/1/10 13:45 
"""

import scrapy

from chouqian.items import HxchemItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
class HxChemSpider(scrapy.Spider):
    name = "hxchem"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [
        "http://www.hxchem.net/company.php?page=%s"%str(i) for i in range(200,3160,1) #
    ]

    #def start_requests(self): #测试cookie
    #    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    #    yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies={'meng':1})

    def parse(self, response):
        base_url = get_base_url(response)
        content = response.body # 乱码处理
        for i in range(100):
            try:
                new_content = unicode(content, 'gbk')
                break
            except Exception, e:
                if 'position' in str(e):
                    error_str = crawlerTool.getRegex('position\s+(\d+-\d+)', str(e))
                    start_index, end_index = int(error_str.split('-')[0]), int(error_str.split('-')[1]) + 1
                    content = content[:start_index] + content[end_index:]
        response_content = new_content

        suburls = crawlerTool.getXpath("//div[@class='ad_content']//dl/dt/a/@href",response_content)
        if len(suburls)<10:
            print('num error',response.url)
        for suburl in suburls:
            suburl = urljoin(base_url,suburl)
            yield scrapy.Request(url=suburl,callback = self.parser_sub)



    def parser_sub(self,response):
        content = response.body # 乱码处理
        for i in range(100):
            try:
                new_content = unicode(content, 'gbk')
                break
            except Exception, e:
                if 'position' in str(e):
                    error_str = crawlerTool.getRegex('position\s+(\d+-\d+)', str(e))
                    start_index, end_index = int(error_str.split('-')[0]), int(error_str.split('-')[1]) + 1
                    content = content[:start_index] + content[end_index:]
        response_content = new_content
        print response.url
        url= response.url
        gywm =crawlerTool.getXpath("//td[@class='goscill22']/table[2]//p/text()",response_content) # 关于我们
        gywm = ''.join(gywm).replace('\n','').replace('\r','')
       # response_content = unicode(response_content, 'gbk') # http://www.hxchem.net/companydetaildesenborn.html 这个就不行了！
        lxwm = crawlerTool.getXpath("//td[@class='goscill22']/table[4]",response_content) # 联系我们
        lxwm = lxwm[0]
        # lxwm = HTMLParser().unescape(lxwm)
        # lxwm=lxwm.encode('utf8')
        data_obj = HxchemItem()
        data_obj['url'] = url
        data_obj['gywm'] = gywm
        data_obj['name'] = crawlerTool.getXpath("//h1/text()",response_content)[0]
        data_obj['lxr'] = crawlerTool.getRegex('联系人：(.*?)<',lxwm)
        data_obj['dz'] = crawlerTool.getRegex('地　址：(.*?)<',lxwm)
        data_obj['yb'] = crawlerTool.getRegex('邮　编：(.*?)<',lxwm)
        data_obj['dh'] = crawlerTool.getRegex('电　话：(.*?)<',lxwm)
        data_obj['sj'] = crawlerTool.getRegex('手　机：(.*?)<',lxwm)
        data_obj['wz'] = crawlerTool.getRegex('网　址：<.*?>(.*?)<', lxwm)
        data_obj['dzyj'] = crawlerTool.getRegex('电子邮件：<.*?>(.*?)<', lxwm)
       # print lxr,dz,yb,dh,sj
        yield data_obj





