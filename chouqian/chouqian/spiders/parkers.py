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

from chouqian.items import ParkersItem
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from urlparse import urljoin
from scrapy.utils.response import get_base_url
from crawl_tool import crawlerTool
from HTMLParser import HTMLParser
import re

class ParkersSpider(scrapy.Spider):
    name = "parkers"  # 唯一标识
    # allowed_domains = ["csdn.net"]
    start_urls = [
'https://www.parkers.co.uk/car-manufacturers/'
    ]

    #def start_requests(self): #测试cookie
    #    # 带着cookie向网站服务器发请求，表明我们是一个已登录的用户
    #    yield scrapy.Request(self.start_urls[0], callback=self.parse, cookies={'meng':1})

    def parse(self, response):
        base_url = get_base_url(response)
        content = response.body # 乱码处理
        manufacturers = crawlerTool.getXpath("//h2/a/@href",content)

        for manufacturer in manufacturers:
            sub_url = 'https://www.parkers.co.uk'+ manufacturer +'specs/'
            yield scrapy.Request(url=sub_url, callback=self.parser_sub)



    def parser_sub(self, response):
        content = response.body
        url = response.url
        # spec_urls = crawlerTool.getXpath('//h4/a/@href',content)
        spec_urls = re.findall('href="(.*?/specs/)"',content)
        for spec_url in spec_urls:
            if not 'http' in spec_url:
                spec_url = 'https://www.parkers.co.uk'+ spec_url
                yield scrapy.Request(url=spec_url, callback=self.parser_spec_url)


    def parser_spec_url(self,response):
        content = response.body
        url = response.url
        FullSpecs_urls = crawlerTool.getXpath('//h3/a/@href', content)
        for spec_url in FullSpecs_urls:
            if not 'http' in spec_url:
                spec_url = 'https://www.parkers.co.uk' + spec_url
                yield scrapy.Request(url=spec_url, callback=self.parser_detail)

    def parser_detail(self,response):
        content = response.body
        url = response.url
        data_obj = ParkersItem()
        data_obj['title'] = crawlerTool.getXpath('//title/text()', content)[0]
        data_obj['url'] = url  # url 中提取名称和model

        urlsplit = url.split('/')
        if len(urlsplit) >4:
            data_obj['name'] = urlsplit[3]
            data_obj['model'] = urlsplit[4]
        data_obj['power'] = crawlerTool.getRegex('Power</th><td>(.*?)</td>',content)
        data_obj['TopSpeed'] = crawlerTool.getRegex('Top Speed</th><td>(.*?)</td>',content)
        data_obj['zerotosixty'] = crawlerTool.getRegex('<th>0-60 mph</th><td>(.*?)</td>', content)
        data_obj['Torque'] = crawlerTool.getRegex('<th>Torque</th><td>(.*?)</td>', content)
        data_obj['co2Emissions'] = crawlerTool.getRegex('<th>CO<sub>2</sub> Emissions</th><td>(.*?)</td>', content)
        data_obj['EuroEmissionsStandard'] = crawlerTool.getRegex('<th>Euro Emissions Standard</th><td>(.*?)</td>', content)
        data_obj['Fuelconsumption'] = crawlerTool.getRegex('<tr><th>Fuel consumption</th><td>(.*?)</td>',
                                                                 content)

        data_obj['Length'] = crawlerTool.getRegex('<tr><th>Length</th><td>(.*?)</td>',
                                                                 content)

        data_obj['Width'] = crawlerTool.getRegex('<tr><th>Width</th><td>(.*?)</td>',
                                                                 content)
        data_obj['Height'] = crawlerTool.getRegex('<tr><th>Height</th><td>(.*?)</td>',
                                                 content)
        data_obj['EngineSize'] = crawlerTool.getRegex('<tr><th>Engine Size</th><td>(.*?)</td>',
                                                 content)
        data_obj['Cylinders'] = crawlerTool.getRegex('<tr><th>Cylinders</th><td>(.*?)</td>',
                                                 content)
        data_obj['FuelType'] = crawlerTool.getRegex('<tr><th>Fuel Type</th><td>(.*?)</td>',
                                                 content)
        data_obj['Transmission'] = crawlerTool.getRegex('<tr><th>Transmission</th><td>(.*?)</td>',
                                                 content)
        data_obj['Doors'] = crawlerTool.getRegex('<tr><th>Doors</th><td>(.*?)</td>',
                                                 content)
        data_obj['Seats'] = crawlerTool.getRegex('<tr><th>Seats</th><td>(.*?)</td>',
                                                 content)
        data_obj['taxcostBasic'] = crawlerTool.getRegex('<tr><th>Monthly company car tax cost \(Basic Rate\)</th><td>(.*?)</td>',
                                                 content).replace('&#163;','£')# £ 是英镑


        # print lxr,dz,yb,dh,sj
        yield data_obj



if __name__ == "__main__":
    from scrapy import cmdline
    sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))
    print 'start spider'
    cmdline.execute("scrapy crawl parkers".split())


