# encoding: utf-8

"""
@author: Meng.ZhiHao
@contact: 312141830@qq.com
@file: cou_qian_spider.py
@time: 2018/1/10 13:45
"""

import scrapy

from chouqian.items import CmocroItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
from ..pipelines import MysqlPipeline3#get_by_unique_value
class CmocroSpider(scrapy.Spider):
    name = "cmocro"  # 唯一标识
    # allowed_domains = ["csdn.net"]

    start_urls = [
         #
    ]
    db_connect = MysqlPipeline3()

    url_cache = [] # 这里用一下内存去重
    for i in xrange(26):
        c1 = chr(i + ord('a'))
        for i in xrange(26):
            c2 = chr(i + ord('a'))
            start_urls .append("https://www.cmocro.com/company_search.php?company=%s%s" % (c1,c2))
    # start_urls = start_urls[:1]


    #def start_requests(self): #测试cookie
    #    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    #    yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies={'meng':1})

    def parse(self, response):
        base_url = get_base_url(response)
        content = response.body # 乱码处理
        for i in range(100):
            try:
                new_content = unicode(content, 'utf8')
                break
            except Exception, e:
                if 'position' in str(e):
                    print str(e)
                    error_str = crawlerTool.getRegex('position\s+(\d+-\d+)', str(e))
                    if '-' in str(e):
                        start_index, end_index = int(error_str.split('-')[0]), int(error_str.split('-')[1]) + 1
                        content = content[:start_index] + content[end_index:]
                    else:
                        start_index  = int(crawlerTool.getRegex('position (\d+)',str(e)))
                        content = content[:start_index] + content[start_index+1:]

        response_content = new_content

        suburls = crawlerTool.getXpath('//div[@class="company_list"]/a/@href',response_content)
        for suburl in suburls:
            suburl = urljoin(base_url, suburl)
            if not self.db_connect.get_by_unique_value(suburl):
                yield scrapy.Request(url=suburl,callback = self.parser_sub)



    def parser_sub(self,response):
        content = response.body # 乱码处理
        # for i in range(100):
        #     try:
        #         new_content = unicode(content, 'gbk')
        #         break
        #     except Exception, e:
        #         if 'position' in str(e):
        #             error_str = crawlerTool.getRegex('position\s+(\d+-\d+)', str(e))
        #             start_index, end_index = int(error_str.split('-')[0]), int(error_str.split('-')[1]) + 1
        #             content = content[:start_index] + content[end_index:]
        response_content = content
        print response.url
        url= response.url
        cfemail = crawlerTool.getXpath('//a[@class="__cf_email__"]/@data-cfemail', content)
        title = crawlerTool.getXpath('//title/text()', content)[0]

        mail = ''
        if cfemail:
            mail = self.get_mail(cfemail[0])
        data_obj = CmocroItem()
        data_obj['url'] = url
        data_obj['mail'] = mail
        data_obj['name'] = title.replace('- CMOCRO','')
       # print lxr,dz,yb,dh,sj
        yield data_obj

    def get_mail(self,mail):
        import execjs
        ctx = execjs.compile("""
         function decode_email(a){ for (e = '', r = '0x' + a.substr(0, 2) | 0, n = 2; a.length - n; n += 2) e += '%' + ('0' + ('0x' + a.substr(n, 2) ^ r).toString(16)).slice(-2); var emailDecoded = decodeURIComponent(e);return emailDecoded}""")
        return ctx.call("decode_email", mail)

